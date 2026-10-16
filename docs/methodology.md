# Data and model methodology

## Version 2026-10-16-v1

Source: City of Medford FY27 ClearGov budget book, updated June 25, 2026, retrieved October 16, 2026. The City budget landing page still labels this book proposed. It has not been reconciled to Council adoption or later amendments. This is a research preview, not an official/current adopted budget.

The source's accessible chart labels were read directly in the browser. `data/build_data.py` preserves the transcribed arrays and generates `data/budget.json`, `data.js`, and `data/records.csv`. Each record carries its source URL, basis and date. FY22–25 are book-reported actuals; FY26–27 are book-reported budgets. Incomplete FY26 actuals are deliberately omitted from the app. No audited-status inference is made. This delivers five years of context, not five completed audited actual years.

44 department/section records, 86 source category series, 516 year/account records. Numeric prime account codes are unknown. Source labels such as Personnel Expenses, Ordinary Expenses and division names are retained rather than invented codes. Duplicate source series are separately named. Missing points stay null. Government-wide debt is not used: only the source's General Fund debt series enters the model. PEG and Water/Sewer are separately displayed and excluded. Chevalier's current allocation is incorporated in Facilities according to the narrative; no stand-alone current amount is invented.

## Reconciliation

Published General Fund revenue: $232,326,737.50. Published expenditure: $232,974,738.86. Source difference: $648,001.36. This is not an established operating deficit.

Imported current General Fund model lines: $231,123,636.89. The $1,851,101.97 remaining difference to the published total is an unassigned reconciliation amount, not a real department. It is held flat in projections. Resident groups are presentation groupings, not a verified crosswalk to the published function chart. The Sankey displays source function totals, and department details retain their own source totals. Do not infer that regrouped department totals match published functions.

## Model

For each account with a known FY27 amount, annual expense = base × (1 + annual driver)^years × department adjustment. Department adjustments begin FY28 and persist. Account-specific growth replaces its shared driver. School appropriation is counted once; benefits remain centrally accounted for. Insurance personnel categories use the insurance driver, not wage growth. Pension uses its own driver. Debt starts flat pending a verified schedule. New capital entries are cash investments, not debt issuance.

Expense starting rates are the median of the three annual changes in aggregate comparable FY22–25 lines for each driver, restricted to positive non-null observations, capped between 0% and 15%. Departments explicitly marked non-comparable/crosswalk-pending are excluded from that estimation. These are transparent mechanical starting points, not causal estimates or validated forecasts. Operating combines ordinary expense and unsplit categories. All can be edited.

Tax receipts use an illustrative percentage plus annual new-growth dollars, initially $2.1M from the book narrative. The property-tax starting amount is not claimed to be a certified levy limit. Excluded debt, levy capacity, the ceiling and the tax recap need a verified bridge before a legal levy calculator or household impact can be added. State aid/local receipts start at a clearly editable 2%; transfers/federal aid are flat, not certified as recurring. New recurring revenue illustrates an override-like addition, growing at 2.5% after its first year; it is not authority to levy.

Headline new funding need = (modeled expense − FY27 published expense) − (modeled revenue − FY27 published revenue). This isolates incremental change rather than converting the unresolved original $648,001.36 source difference into a claimed deficit. Recurring gap excludes one-time investments. A user-entered hypothetical reserve pool covers positive incremental gaps up to an annual cap and remaining balance. Reserves never increase recurring revenue and cannot be spent twice.

Scenario JSON and share links include the data version. Older versions are rejected rather than silently recalculated against a new baseline. Inputs are bounded; text is escaped before rendering. Saving is explicit and browser-local. Shared URLs contain scenario assumptions, not private account data.

## Outstanding gates

1. Obtain adopted Council appropriation orders and all subsequent amendments, including Law.
2. Reconcile departmental and function mappings and the $1.85M unassigned amount.
3. Obtain numeric account codes and detailed DPW/Facilities/Building accounts.
4. Cross-check historical amounts against prior-year books and audited actuals.
5. Reconcile certified levy, final aid, assessments, overlays, transfers and one-time sources.
6. Replace debt and pension percentage placeholders with adopted schedules.

No official budget balance, tax bill, legal borrowing capacity, or available reserve balance is claimed.
