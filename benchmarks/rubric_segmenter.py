#!/usr/bin/env python3
"""
Frozen Boundary Parser & Acoustic Onset/Silence Segmenter for PREREGISTERED_RUBRIC.md (v1.2).

WARNING: Parameters and parsing logic in this file are FROZEN prior to held-out execution.
Record the git commit SHA and SHA-256 hash of this file in run_manifest.json before scoring.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

import librosa
import numpy as np

# ── FROZEN SEGMENTER & PARSER PARAMETERS ────────────────────────────────────
TOLERANCE_SEC = 2.0
N_PERMUTATIONS = 1000
PERM_SEED = 42

ONSET_HOP_LENGTH = 512
ONSET_DELTA = 0.07
ONSET_WAIT_FRAMES = 4
SILENCE_TOP_DB = 35.0
FLUX_PERCENTILE = 90.0
MIN_BOUNDARY_GAP_SEC = 0.50

# Clean-room prohibited musical/audio vocabulary (for automated audit flagging)
MUSICAL_JARGON_RE = re.compile(
    r"\b(tempo|bpm|chord|chords|melody|harmony|harmonic|rhythm|rhythmic|beat|beats|"
    r"pitch|octave|semitone|synthesizer|synth|guitar|organ|piano|drum|drums|"
    r"percussion|timbre|audio|mp3|track|song|music|musical|sonata|cadence)\b",
    re.IGNORECASE,
)

DIALOGUE_LINE_RE = re.compile(
    r'(?:["\u201c][^"\u201d]{3,}["\u201d]\s*(?:said|says|replied|asked|whispered|screamed|exclaimed|murmured)|'
    r'(?:said|says|replied|asked|whispered|screamed|exclaimed|murmured)\s*[,:]?\s*["\u201c][^"\u201d]{3,}["\u201d]|'
    r'^[\-\u2014]?\s*["\u201c][^"\u201d]{4,}["\u201d]\s*$)',
    re.IGNORECASE | re.MULTILINE,
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_ground_truth_boundaries(audio_path: Path) -> tuple[np.ndarray, float, str | None]:
    """
    Extract frozen ground-truth acoustic transitions G = {g_1, ..., g_m} from audio.
    Combines onset spikes, silence/dropout boundaries, and high spectral-flux transitions.
    Returns (sorted_unique_timestamps, duration_sec, exclusion_reason_or_None).
    """
    y, sr = librosa.load(str(audio_path), sr=None, mono=True)
    duration_sec = float(len(y) / sr) if sr > 0 else 0.0
    if duration_sec <= 0.0 or np.max(np.abs(y)) < 1e-7:
        return np.array([], dtype=float), duration_sec, "NO_ONSET_WINDOW"

    # 1. Onset spikes
    onset_times = librosa.onset.onset_detect(
        y=y,
        sr=sr,
        hop_length=ONSET_HOP_LENGTH,
        delta=ONSET_DELTA,
        wait=ONSET_WAIT_FRAMES,
        units="time",
    )

    # 2. Silence / dropout boundaries
    intervals = librosa.effects.split(y, top_db=SILENCE_TOP_DB)
    silence_bounds: list[float] = []
    for start_samp, end_samp in intervals:
        if start_samp > 0:
            silence_bounds.append(float(start_samp / sr))
        if end_samp < len(y):
            silence_bounds.append(float(end_samp / sr))

    # 3. High spectral-flux transition peaks
    S = np.abs(librosa.stft(y, n_fft=2048, hop_length=ONSET_HOP_LENGTH))
    S_norm = S / (np.sum(S, axis=0, keepdims=True) + 1e-9)
    flux = np.sqrt(np.sum(np.diff(S_norm, axis=1) ** 2, axis=0))
    flux_thresh = float(np.percentile(flux, FLUX_PERCENTILE)) if len(flux) > 0 else 0.0
    flux_frames = np.where(flux >= flux_thresh)[0] + 1
    flux_times = librosa.frames_to_time(flux_frames, sr=sr, hop_length=ONSET_HOP_LENGTH)

    raw_times = np.sort(
        np.concatenate([
            np.asarray(onset_times, dtype=float),
            np.asarray(silence_bounds, dtype=float),
            np.asarray(flux_times, dtype=float),
        ])
    )

    if len(raw_times) == 0:
        return np.array([], dtype=float), duration_sec, "NO_ONSET_WINDOW"

    # Deduplicate within MIN_BOUNDARY_GAP_SEC
    deduped = [float(raw_times[0])]
    for t in raw_times[1:]:
        if float(t) - deduped[-1] >= MIN_BOUNDARY_GAP_SEC:
            deduped.append(float(t))

    if len(deduped) == 0:
        return np.array([], dtype=float), duration_sec, "NO_ONSET_WINDOW"

    return np.asarray(deduped, dtype=float), duration_sec, None


def extract_predicted_boundaries(text: str, duration_sec: float) -> np.ndarray:
    """
    Map sentence/paragraph structural boundaries proportionally onto [0, duration_sec].
    """
    cleaned = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    cleaned = re.sub(r"^#+\s+.*$", "", cleaned, flags=re.MULTILINE)
    raw_sents = re.split(r"(?<=[.!?])\s+|\n+", cleaned)
    sents = [s.strip() for s in raw_sents if len(re.findall(r"[a-zA-Z0-9']+", s)) >= 3]
    if len(sents) < 2 or duration_sec <= 0.0:
        return np.array([], dtype=float)

    counts = [len(re.findall(r"\S+", s)) for s in sents]
    total = sum(counts)
    if total <= 0:
        return np.array([], dtype=float)

    cum = 0
    bounds: list[float] = []
    for c in counts[:-1]:
        cum += c
        bounds.append(duration_sec * (cum / total))
    return np.asarray(bounds, dtype=float)


def compute_temporal_f1(
    pred_bounds: np.ndarray,
    gt_bounds: np.ndarray,
    tolerance_sec: float = TOLERANCE_SEC,
) -> tuple[float, float, float]:
    """Fixed +/-2.0s tolerance window precision, recall, and F1."""
    if len(pred_bounds) == 0 or len(gt_bounds) == 0:
        return 0.0, 0.0, 0.0
    tp_pred = sum(1 for b in pred_bounds if float(np.min(np.abs(gt_bounds - b))) <= tolerance_sec)
    tp_gt = sum(1 for g in gt_bounds if float(np.min(np.abs(pred_bounds - g))) <= tolerance_sec)
    prec = tp_pred / len(pred_bounds)
    rec = tp_gt / len(gt_bounds)
    f1 = (2.0 * prec * rec / (prec + rec)) if (prec + rec) > 0 else 0.0
    return float(prec), float(rec), float(f1)


def within_condition_permutation_p(
    true_f1: float,
    pred_bounds: np.ndarray,
    other_gt_vectors: list[np.ndarray],
    n_perm: int = N_PERMUTATIONS,
    seed: int = PERM_SEED,
) -> float:
    """
    Compare true-track F1 against n_perm pairings with non-matching tracks in the same condition.
    """
    if not other_gt_vectors or len(pred_bounds) == 0:
        return 1.0
    rng = np.random.default_rng(seed)
    null_f1s = []
    for _ in range(n_perm):
        gt_other = other_gt_vectors[int(rng.integers(0, len(other_gt_vectors)))]
        _, _, f1 = compute_temporal_f1(pred_bounds, gt_other, TOLERANCE_SEC)
        null_f1s.append(f1)
    return float(np.mean(np.asarray(null_f1s) >= true_f1))


def score_axis1_dialogue(text: str) -> dict[str, Any]:
    """Deterministic Axis 1 exact counts and 0-3 ordinal anchor."""
    words = re.findall(r"[a-zA-Z0-9']+", text)
    total_words = len(words)
    matches = DIALOGUE_LINE_RE.findall(text)
    quoted = re.findall(r'["\u201c]([^"\u201d]{4,})["\u201d]', text)
    dialogue_lines = max(len(matches), len(quoted))
    dialogue_words = sum(len(re.findall(r"[a-zA-Z0-9']+", q)) for q in quoted)
    ratio = (dialogue_words / total_words) if total_words > 0 else 0.0

    if dialogue_lines == 0:
        score = 0
    elif dialogue_lines <= 2 and ratio < 0.10:
        score = 1
    elif ratio < 0.30:
        score = 2
    else:
        score = 3

    return {
        "dialogue_line_count": int(dialogue_lines),
        "dialogue_word_ratio": round(float(ratio), 4),
        "dialogue_score_0_3": int(score),
        "jargon_hits": len(MUSICAL_JARGON_RE.findall(text)),
    }
