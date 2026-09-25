# Custom GPT Setup — Music For Robots Explorer

## Steps (takes ~10 minutes)

1. Go to https://chatgpt.com/gpts/create
2. Fill in:
   - **Name**: Music For Robots Explorer
   - **Description**: Explore the M4R catalog — music written by a human for robots, reviewed by two AI critics in real time. Query spectral analysis, harmonic structure, pitch class sets, and timed reviews.
   - **Instructions**: Copy the contents of `instructions.md` in this folder
3. Under **Actions**, click "Create new action":
   - **Authentication**: None
   - **Schema**: Paste the contents of `action-schema.json` in this folder
   - Click "Test" on getCatalog to verify it works
4. **Conversation starters** (suggested):
   - "What tracks are in the catalog?"
   - "Show me the analysis for Foundationoff"
   - "What did Vincent think of Binded Time?"
   - "Compare the harmonic complexity across all tracks"
   - "Which track has the highest compression loss?"
5. **Knowledge**: Leave empty (the GPT reads live data from the API)
6. Click **Create** → **Publish** → **Everyone**

## How It Updates

The GPT reads from `raw.githubusercontent.com/luchtan-GIT/m4r-data/main/` on every query. When new tracks are pushed to the repo, the GPT automatically sees them — no GPT update needed.

## Testing

After creating, try:
- "List all tracks" → should return 8 tracks
- "Get the manifest for foundationoff" → should return full analysis + reviews
- "What pitch classes does Robographia use?" → should answer from the manifest data
