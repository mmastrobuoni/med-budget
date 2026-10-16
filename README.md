# Medford Budget Lab

A static, resident-facing budget explorer and scenario simulator in Mike Mastrobuoni's School Committee branding.

**Research preview:** FY27 book figures are not reconciled to adopted appropriations. The interface discloses the $648,001.36 revenue/expenditure source difference and $1,851,101.97 unassigned department crosswalk difference. It reports new funding needs since FY27, not a finding of a City deficit.

## Features
- Published revenue/spending allocation ribbons and accessible tables.
- 44 department/section records and 516 account/year records with source links.
- FY22–FY27 budget history; FY22–FY25 actual history separately.
- Five-year projections, editable expense/revenue assumptions, department and account overrides.
- Recurring/one-time investments, recurring revenue, finite reserve use.
- Explicit browser-local save, reset, JSON import/export, shareable scenario URLs.
- No external runtime dependencies, account registration, or build step.

## Run
Open `index.html` or serve the root with a static server. Publish root of `main` with GitHub Pages. All assets are local.

## Data and tests
Run `python3 data/build_data.py` to regenerate data from the recorded source transcription. Run `node tests/model.test.cjs` for calculation and reconciliation checks.

See [methodology](docs/methodology.md) and [project brief](docs/project-brief.md). Numeric prime-account codes, adoption reconciliation, and final FY26 actuals remain outstanding.
