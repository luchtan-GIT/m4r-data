#!/usr/bin/env bash
# Music For Robots Laboratory (#M4R) — Private Turn-0 Specimen Fetcher
# Downloads Michael Luchtan's "Stuttering Packets" (3:20, CC-BY-4.0) into a
# process-private directory (0700) with restricted permissions (0600).
set -euo pipefail

CACHE_BASE="${XDG_CACHE_HOME:-$HOME/.cache}/m4r_turn0"
mkdir -p "$CACHE_BASE"
chmod 700 "$CACHE_BASE"

TARGET="$CACHE_BASE/stuttering-packets.mp3"
URL="https://raw.githubusercontent.com/luchtan-GIT/m4r-data/main/tracks/stuttering-packets/audio.mp3"

if [[ ! -s "$TARGET" ]]; then
  TMP_FILE=$(mktemp "$CACHE_BASE/tmp_XXXXXX.mp3")
  curl --fail -s -L "$URL" -o "$TMP_FILE"
  chmod 600 "$TMP_FILE"
  mv "$TMP_FILE" "$TARGET"
fi

BYTES=$(wc -c < "$TARGET" | tr -d ' ')
if [[ "$BYTES" -lt 1000000 ]]; then
  echo "ERROR: Downloaded file too small ($BYTES bytes). Aborting." >&2
  rm -f "$TARGET"
  exit 1
fi

echo "M4R_TURN0_AUDIO=$TARGET"
echo "Ready for Turn-0 binary multimodal ingestion (Stuttering Packets, 199.9s, $BYTES bytes)."
