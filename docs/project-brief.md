# Medford Budget Lab — project brief

October 16, 2026

## Purpose
An independent resident budget simulator by Mike Mastrobuoni, Medford School Committee. Understand where revenue goes, project service costs, add investments, and explore how to fund them. Visitors edit personal scenarios, not published source data. Use the established navy (#002855), gold (#FFC72C), cream/white branding and verified logo assets, in the visual family of what-2-5-can-buy.

## Experience
- Explore: revenue → General Fund → department Sankey, switchable to spending categories, with department/prime-account drilldown and accessible tables. Unrestricted sources flow through the shared fund rather than implying earmarks.
- Project: five historical years plus current appropriations and five projected years. Editable cost drivers with department/account overrides. Clearly distinguish actuals, appropriations, and forecasts.
- Invest: add recurring or one-time costs with start years; staffing includes benefits without duplicating central benefits. Capital separates cash spending and annual debt service.
- Balance: show annual gap, recurring balance, reserves used, and the next-year consequences. Separate levy growth, new growth, state aid, local receipts, overrides, and one-time funding.
- Save and share: local scenarios, reset, export, and shareable assumptions. Published baseline stays unchanged.

## Data
Target FY2022–FY2026 history and FY2027 baseline, subject to availability. Record fiscal year, fund, department, prime account, optional detailed object, amount, reporting basis, source URL/page/order, source version, retrieval date, and review status. Preserve original codes alongside a normalized crosswalk. Missing is null, not zero. Keep actual spending, original budget, amended budget, and proposed budget as separate series. Do not double-count parent totals, transfers, school detail, or centrally budgeted benefits. Water/Sewer and restricted funds stay separate from General Fund balancing.

Historical growth informs defaults but does not automatically become the forecast. Flag reorganizations and one-time items. Use separate drivers for wages, health insurance, pension assessments, operating costs, utilities, schools, and scheduled debt. Forecast levy limits separately from actual levy after checking official levy worksheets. Show assumptions, source dates, and applicable approval requirements.

## Sources and reconciliation
- https://www.medfordma.org/mayors-office/city-budget
- https://city-medford-ma-budget-book.cleargov.com/21444/fund-summaries/general-fund
- https://www.medfordma.org/departments/finance
- https://medfordma.portal.civicclerk.com/
- https://www.mass.gov/info-details/municipal-finance-trend-dashboard-reports

Earlier project research dated October 7 transcribed FY27 ClearGov revenue of $232,326,737.50 and expenditure of $232,974,738.86. The $648,001.36 difference is an unresolved source reconciliation, NOT an established operating deficit. Re-verify these research observations and reconcile the book to adopted Council appropriations, amendments, funding sources, and tax-rate-setting scope before loading a production baseline. The earlier review found a proposed label on the City landing page; do not silently relabel proposed numbers as adopted.

## Implementation
Static GitHub Pages-compatible application with versioned JSON/CSV data. Separate source register, historical records, baseline, assumptions, and scenarios. One calculation engine feeds charts, tables, and exports. Sankey allocation and time-series revenue/spending/gap charts; visible historical-to-forecast boundary. Source links and downloadable tables throughout.

## Completion criteria
Reconciled annual totals; documented classifications; no duplicate spending; conserving flow diagrams; verified compounding and investment timing; reserve depletion modeled; scenario reset/export round trips; keyboard/mobile usability; clear independent-project attribution and baseline as-of date.

## Status
Scope and repository access established. Earlier research located. Data extraction, current-appropriation reconciliation, application implementation, and deployment are outstanding. No working simulator has been published.
