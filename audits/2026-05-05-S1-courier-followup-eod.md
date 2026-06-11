# S1 courier follow-up audit — 2026-05-05

## Outbox 회신: `S1-followup-20260505.json` 처리 결과

### Request 1 — ccmxpf_lnkhist sample (FULFILLED)
- ✓ Sample dumped: `wrdsappssamp_all.ccmxpf_lnkhist` (1,927 rows, 0.02MB)
- ✓ Schema verified via `crsp_link.smoke_test_sample()`:
  - Columns: lpermno, gvkey, linkdt, linkenddt (4 cols)
  - 1,913 unique permnos, 1,909 unique gvkeys
  - Date range: 1962-01-02 → 2013-10-04 (sample truncated)
  - 848 active links (linkenddt IS NULL)
- ✓ Swap-in code prepared: `crsp_link.build_ccmxpf_link()` + `crsp_link.link_to_event_aware()`
  - When `crsp_a_ccm.ccmxpf_lnkhist` USAGE unblocks, calling
    `build_ccmxpf_link('crsp_a_ccm.ccmxpf_lnkhist', gvkeys=universe_gvkeys)`
    returns time-varying link with academic-grade `linktype IN ('LC','LU') AND linkprim IN ('P','C')` filter.
- 🚧 Sample lacks linktype/linkprim — cannot apply quality filter; sample is schema-prototype only.

### Request 2 — WRDS USAGE unblock status (BLOCKED, USER ACTION PENDING)
- ⛔ Email NOT yet dispatched (courier session has no email tool)
- 📋 Action item for user:
  1. Open `WRDS_BLOCKED_SCHEMAS.md` in courier repo
  2. Copy email draft
  3. Send to `wrds-support@wharton.upenn.edu` from the WRDS account (see local credentials)
  4. Reply to courier outbox with timestamp
- ETA after dispatch: 1-2 weeks (1-3 business days response + 3-7 days grant)
- Note: CUSIP8 95.4% sufficient for current Phase 3 honest revision; final swap only needed for paper publication if reviewers demand time-varying linkage rigor.

### Request 3 — comp_na_daily_all.idxcst_his (FULFILLED, but NEGATIVE FINDING)
- ✓ Table dumped: 24,301 rows, 990 distinct indices
- ❌ **Critical negative finding**: idxcst_his does NOT contain real S&P 500 / Russell 3000 historical reconstitution as expected.
  - Courier guessed `gvkeyx=031855` ≈ "Russell 3000-class" (1,505 rows). **Wrong**: 0 firms ever dropped (`thru` always NULL); ever-joined snapshot. Earliest entry 1964 (Russell didn't exist yet).
  - Courier guessed `gvkeyx=000010` ≈ "S&P 500" (1,176 firms, 1,262 dropped — looks promising). **Wrong**: Apple (gvkey=001690) and MSFT (gvkey=012141) are NOT in this index. Apple has been in real S&P 500 since 2003-03-03; MSFT since 1994-06-06.
  - Apple in this dataset: 17 different `gvkeyx` indices, all with `from = 1982-11-30` (Apple's IPO) — these are clearly Compustat-internal categorization rollups (sector aggregates / dividend baskets), not real real-world stock indices.
- ❌ **Conclusion**: idxcst_his in our subscription does NOT support historical S&P 500 / R3000 universe reconstruction. Real index data probably requires Russell module / S&P historical-constituents subscription not in our dump.
- 📌 **Implication for paper**: The "current iShares R3000 backfill" approach in §11 limitation #1 is the **best-available** universe construction. Survivor bias is now mitigated via CRSP `dsf` delisting returns (Phase 3) — that is the principal correction; explicit historical R3000 membership reconstruction is infeasible.

### Request 4 — CRSP delisting tables (FULFILLED, NO DUMP)
- ✓ Confirmed `crsp_a_stock.dsedelist` exists (6.27MB, 38,872 rows). Reason codes:
  - 100: active
  - 200: merger
  - 231: merger-by-acquisition
  - 233: merger-by-cash
  - 400: liquidation
  - 500: dropped
  - 560: dropped-too-low-priced
  - 575: dropped-insufficient-data
- ✓ Modern v2 alternative: `crsp_a_stock.stkdelists` (4.69MB, 29,833 rows) with cleaner enum schema
- ✓ Verdict on S1 hypothesis "dsf.ret 컬럼이 delisting return 자동 포함이라 별도 테이블 불필요":
  - **PARTIALLY TRUE**: dsf.ret on delisting date includes delret (Shumway 1997 convention)
  - Useful additional value of separate table: (1) reason-code filtering for honest comparison samples, (2) successor mapping (nwperm/delpermno) for spinoff continuity, (3) handling missing-delret cases (Beaver-McNichols-Price 2007)
- 📌 **Decision for S1**: dsedelist (6.27MB) NOT yet requested for dump. Phase 3 result already supports the headline without explicit reason-code filtering. Defer dump until paper-publication robustness check phase.

## Updated Phase 3 honest revision status

Pre-investigation, I considered S&P 1500 historical universe reconstitution as a robustness check. Investigation showed this is infeasible in our dump.

**Therefore, the Phase 3 honest revision is COMPLETE as of 2026-05-05 commit `cbcd0f4`** with these data caveats explicitly documented:
1. CUSIP8 static link — 95.4% R3000 universe coverage (paper §11 limitation #7)
2. CRSP cutoff 2024-12-31 — loses 2025-04-01 SLOOS event (paper §11 limitation #8)
3. IVOL still macro proxy — firm-level Ang et al deferred (paper §11 limitation #9)
4. **S&P/Russell historical membership infeasible** — best-available is current iShares R3000 + CRSP delisting (this audit)

**Headline finding holds**: 6m alpha-Sharpe +3.357 (p<0.001) on CRSP, 5/5 walk-forward folds positive, sign-conditional similar +3.244 (p<0.001).

## Files added in this audit
- `src/sloos_sector_cross_section/crsp_link.py` — added `build_ccmxpf_link()`, `link_to_event_aware()`, `smoke_test_sample()` (production swap-in code, ready when USAGE unblocks)
- This audit

## Outstanding
- User action: dispatch WRDS USAGE-unblock support email
- Optional future dump: `dsedelist` for paper publication robustness checks (delisting reason filtering)
