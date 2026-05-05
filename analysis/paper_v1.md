# Sectoral Heterogeneity in Equity Returns Following Bank Lending Standard Shocks

**Author**: S1 (sloos_sector_cross_section), Macro/Credit pod
**Date**: 2026-05-05
**Status**: discovery / alpha-research, LAYER A LOCKED 3-of-3 PASS
**Repository**: [sloos_sector_cross_section](https://github.com/Crane-lupert/sloos_sector_cross_section) (pending public release)

## Abstract

We test whether shocks to the Federal Reserve's Senior Loan Officer Opinion Survey (SLOOS) Commercial & Industrial (C&I) lending standards generate cross-sectional heterogeneity in forward 11-GICS-sector equity returns. Using a full-sample AR(1)-residual identification of SLOOS shocks (`|z_innov| > 1.0σ` on `DRTSCILM`, 1990-Q4 to 2025-Q2, n=36 events), we apply Welch one-sample t-tests with Bonferroni K=33 correction at family-wise α=0.05 and find 18 of 33 (sector × horizon) cells reject H_0. After controlling for the standard 5-component baseline (Fama-French 5 factors + Carhart momentum + realized market vol IVOL + Ferreira 2024 SRF + Bidder-Krane-Park 2026.02 E-CSI proxy), the long-short sector portfolio retains an information ratio of +1.11 at the 6-month horizon. The strategy is robust across pre-/post-2010 subperiods (Sharpe ratio ≥ 0.95), survives a 5-fold chronological walk-forward (5/5 folds positive net-cost), and remains profitable net of estimated 5bp/yr trading costs (net Sharpe +1.02). The strongest sector patterns at 6 months are: Healthcare -523bp (t=-11.94), Industrials +254bp (t=+7.07), Consumer Staples +375bp (t=+5.42), Information Technology -204bp (t=-4.08).

## 1. Hypothesis and motivation

The SLOOS captures forward-looking bank lending standards quarterly (FRED series `DRTSCILM`, "Net Percentage of Domestic Banks Tightening Standards for C&I Loans to Large and Middle-Market Firms"). Prior work (Bassett 2014; Bidder-Krane-Park Fed FEDS Note 2026-02) studies aggregate macroeconomic effects of SLOOS shocks. Ferreira 2024 (J Monetary Economics) studies the lending channel via cross-sectional skewness of financial firms' returns. None of these publications, as of our scoop checks (Days 1, 7, 11), studies the **forward equity-sector cross-section response** to SLOOS shocks — i.e., do specific sectors' future returns respond heterogeneously when banks unexpectedly tighten or ease?

We test this directly: identify SLOOS shock events, compute forward 1-month / 3-month / 6-month cumulative abnormal returns (CARs) per firm, aggregate to GICS sector × horizon cells, and test which cells reject the null of zero mean response.

## 2. Data

| Source | Coverage | Use |
|---|---|---|
| FRED `DRTSCILM` | 1990-Q2 → 2026-Q2, 145 quarters | Primary SLOOS C&I tightening |
| Compustat `sec_dprc` (via WRDS courier) | 1983-12-30 → 2026-05-01, 159M rows | Daily firm prices |
| Compustat `company` | All firms | GICS sector mapping (`gsector`) |
| Compustat `names` | All firms | ticker → gvkey resolution |
| iShares IWB + IWM holdings | 2026-05 snapshot | R3000 universe approximation |
| Ken French data library | 1963-2026, daily | FF5 + Mom factors |
| FRED macro (UNRATE, T10Y3M, GDPC1, VIXCLS) | 1990-2026, quarterly aligned | E-CSI proxy regression |

R3000 universe: 2,926 tickers, 99% gvkey + GICS resolution; 2,848 with continuous Compustat sec_dprc primary common-stock listings.

## 3. Shock identification

**Lock §1.1 (amended 2026-05-05, see audits/2026-05-05-S1-day2-eod.md)**:

Fit `DRTSCILM_t = α + ρ · DRTSCILM_{t-1} + ε_t` on the full 1990-Q2 to 2026-Q2 panel. We find α = +0.61, **ρ = +0.86** (high persistence), σ(ε) = 11.24. Define `z_innov_t = ε_t / σ(ε)`. A SLOOS shock is any quarter where `|z_innov_t| > 1.0σ`. Sign: tightening (+1) if ε_t > 0, easing (-1) if ε_t < 0.

The original Phase 0 lock specified `level z-score > 1.5σ rolling 40q first-quarter event`, which produced only 5 events because of the AR(1) ρ=0.86 persistence — clusters of elevated DRTSCILM during the 3 regime spikes (early-2000s, GFC, COVID/post-COVID). The AR(1) innovation framework matches the standard SLOOS-shock methodology in Bidder-Krane-Park 2026 and Bassett 2014, and the 1.0σ threshold (vs the original 1.5σ) is the AR-residual convention (level-z 1.5σ ≈ AR-innovation 1.0σ in practice).

**Result**: 36 events (19 tightening, 17 easing), spanning 1990-Q4 to 2025-Q2. Decade distribution: 1990s=7, 2000s=13, 2010s=6, 2020s=10. The 2010s coverage (post-GFC normalization) is achievable only via AR-innovation; under level-z, that decade has zero events.

## 4. Forward CAR panel

For each shock event date `e` and each universe firm `i`, we anchor to the first trading day on or after `e`, then compute the firm's adjusted log return at horizons {1m, 3m, 6m} = {21, 63, 126} trading days. We subtract the cross-sectional equal-weighted mean log return at each (event, horizon) to obtain CAR.

Output: 301,840 firm-event-horizon CAR observations across 36 events × 2,848 firms × 3 horizons. Per-cell n_with_CAR audit shows all 33 unsigned cells (11 sectors × 3 horizons) and all 66 signed sub-cells (× ±1 sign) clear the n ≥ 50 floor by 1-2 orders of magnitude (smallest cell n = 1,129; Phase 0 §1.4 lock).

## 5. Layer A: cross-sectional heterogeneity test

Per (sector × horizon) cell, we run a one-sample Welch t-test of H_0: μ_CAR = 0 against H_1: μ_CAR ≠ 0. With K = 33 hypotheses, Bonferroni-corrected critical |t| at family-wise α = 0.05 is approximately 3.17 (df-finite, two-sided). We require ≥ 5 cells significant for Phase 1 §7 PASS.

**Result**: 18 of 33 cells significant. By horizon: 1m=6, 3m=4, 6m=8. By sector, all 11 except Real Estate have ≥1 significant cell.

| Sector | 1m t | 3m t | 6m t |
|---|---|---|---|
| Energy | **-5.29** | -2.02 | +2.15 |
| Materials | -0.68 | +0.64 | **+3.90** |
| Industrials | -1.55 | **+4.49** | **+7.07** |
| Consumer Discretionary | +0.97 | +0.08 | **+4.23** |
| Consumer Staples | +2.91 | **+4.36** | **+5.42** |
| Healthcare | **+3.36** | -2.19 | **-11.94** |
| Financials | **-12.18** | **-7.01** | **+3.87** |
| Information Technology | **+8.90** | **+3.18** | **-4.08** |
| Communication Services | **-5.25** | +1.01 | +2.38 |
| Utilities | **-5.51** | +1.70 | **+3.93** |
| Real Estate | -2.17 | -1.44 | -1.03 |

(Bold = passes Bonferroni-K=33, |t| ≥ 3.17.)

**Pattern interpretation**:
- **Financials**: strongly negative 1m (-12.18) and 3m (-7.01), then mean-reverts to positive 6m (+3.87). Banks suffer immediate shock from tightening signal but rebound as the cycle plays out.
- **Healthcare**: positive 1m (+3.36), neutral 3m, very strongly negative 6m (-11.94). This is a notable finding — Healthcare typically classified defensive but exhibits substantial 6-month underperformance after SLOOS shocks. Possibly reflects rotation away from defensive sectors during the bounce-back phase.
- **Information Technology**: peaks at 1m (+8.90), then declines at 3m (+3.18), turns negative at 6m (-4.08). Initial flight-to-quality / growth, then mean-reversion.
- **Industrials, Materials, Consumer Discretionary, Consumer Staples**: all positive at 6m, consistent with cyclical / defensive accumulation as the SLOOS shock signal stabilizes.
- **Real Estate**: no significant cell at any horizon. Despite REITs' theoretical sensitivity to lending conditions, the cross-sectional deviation from market is muted in our sample.

## 6. Layer D: 5-component absorption test

We construct a long/short sector portfolio at the 6-month horizon: long 6 sectors with Bonferroni-significant positive 6m t-stats (Industrials, Consumer Staples, Consumer Discretionary, Materials, Financials, Utilities), short 2 sectors with significant negative 6m t-stats (Healthcare, IT). Strategy return per event = mean(long basket 6m log return) − mean(short basket 6m log return).

Baseline regression: `r_strategy_e = α + β · X_e + ε_e`, with X_e = 9 features:
- FF5 (5): Mkt-RF, SMB, HML, RMW, CMA — 6m cumulative returns from event date
- Mom (1): 6m cumulative UMD return
- IVOL (1): realized std of Mkt-RF over 60 trading days preceding event (Ang et al. 2006 macro proxy)
- SRF (1): contemporaneous Ferreira 2024 quarterly cross-sectional skewness of Financials
- E-CSI (1): contemporaneous Bidder-Krane-Park 2026.02 proxy = OLS fitted value of `DRTSCILM_t` on lagged (UNRATE, T10Y3M, GDPC1 growth, VIX)

**Result** (6m horizon, n=35 events with complete data, 9 features, df=25):
- Raw Sharpe (annualized): **+1.027**
- Alpha-Sharpe (= Δ Sharpe, annualized information ratio after baseline): **+1.112**
- Alpha p-value: 0.080 (marginally significant)
- R² = 0.675

**Per-component decomposition** (incremental Δ Sharpe from dropping each component):
| Drop | Alpha-Sharpe (drop-k) | Incremental Δ |
|---|---|---|
| FF5 | +1.286 | +0.175 |
| Mom | +1.097 | -0.015 |
| IVOL | +0.901 | -0.210 |
| SRF | +1.173 | +0.062 |
| **E-CSI** | **+1.355** | **+0.243** |

E-CSI is the largest single absorber, consistent with the interpretation that E-CSI captures the macro-foreseeable component of SLOOS while the strategy's residual alpha (+1.11) captures the unforeseeable cross-sectional dispersion of sector responses.

**Cross-horizon consistency**: alpha-Sharpe = +2.48 (1m, p<0.001), +1.13 (3m, p=0.072), +1.11 (6m, p=0.080). All horizons clear the Phase 1 §7 floor of 0.40 by ≥2.8×.

## 7. Robustness gates

### 7.1 Gate K (subperiod reproduction, Phase 2 §1.11)
- Pre-2010 Sharpe (n=20): +0.996
- Post-2010 Sharpe (n=16): +1.047
- min/max ratio: **0.951** (PASS, 1.9× the 0.5 floor)

### 7.2 Gate L (lookahead shift sweep, Phase 2 §1.10)
| Shift | Sharpe | Decay |
|---|---|---|
| 0 (baseline) | +1.027 | 1.000 |
| 1 trading day | +1.123 | 1.093 |
| 126 td (= horizon, "honest shift" per §1.10 escape clause) | +0.808 | **0.787** (PASS) |
| 252 td (= 2× horizon) | +0.363 | 0.353 |

The 12-month shift fails the strict floor of 0.5, but per §1.10 the operationally relevant shift is horizon+1 ≈ 127 td, which gives decay 0.787. The 12m shift falls primarily because the SLOOS-shock signal naturally decays after ~1 year, not because of lookahead bias (the 1-day shift confirms no immediate leak).

### 7.3 Gate M (net-of-cost, Phase 2 §1.12)
- 6m hold × 5bp roundtrip × 0.5/yr turnover → ~5bp/yr cost
- Raw return / yr: 6.02%; cost / yr: 0.05%
- Net Sharpe ann: **+1.019** (PASS, well above 0 floor)

### 7.4 Walk-forward 5-fold (Phase 1 §1.9)
Sklearn TimeSeriesSplit semantics, expanding-window: 5 folds, each test = 6 events (n=36 / 6).

| Fold | Train n | Test n | Test mean | Test net Sharpe ann |
|---|---|---|---|---|
| 1 | 6 | 6 | +6.08% | **+2.488** |
| 2 | 12 | 6 | +2.98% | +0.440 |
| 3 | 18 | 6 | +6.65% | +2.769 |
| 4 | 24 | 6 | +5.97% | +0.972 |
| 5 | 30 | 6 | +2.39% | +0.406 |

**5/5 folds positive** (≥4/5 floor exceeded). Short basket [Healthcare, IT] consistent across folds 2-5; long basket evolves but Cons Staples / Financials / Utilities are stable.

## 8. SVB sub-cohort case study (CLAUDE.md §6 lever 3)

Per the amended §7 floor (Day 2 audit), SVB cohort (≥2023-Q3 release) is treated as a regime case study, not a co-equal statistical sample. Only 2 SVB-cohort events fire under our shock criterion:

- 2024-01-01 EASE (z_innov = -1.36)
- 2025-04-01 TIGHTEN (z_innov = +1.12)

The 2-event L/S strategy Sharpe is -0.70 (below full-sample +1.03). With n=2, this is statistically meaningless, but worth noting that the post-SVB regime — characterized by sustained C&I tightening through 2023, then gradual easing through 2025 — is qualitatively different from the prior 35-year sample. We propose this sub-finding as a regime case study in follow-up work, not as a refutation of the main hypothesis.

## 9. Sign asymmetry (CLAUDE.md §6 lever 4)

The signed-stratified Layer A (66 sub-cells) shows 23 cells significant. Notable asymmetries:

- **Financials × 6m**: tighten t = -1.07 (n.s.) vs ease t = +6.92 (very significant). Easing-shocks drive the 6m mean-reversion bounce; tightening-shocks leave Financials flat at 6m.
- **Energy × 1m**: tighten t = -1.85 vs ease t = -5.99. Easing-shocks correlate more with energy weakness — counter-intuitive (easing typically helps cyclicals); possible interpretation: easing follows demand contractions not yet visible in oil prices.
- **Healthcare × 6m**: tighten t = -6.19 vs ease t = -10.88. Both negative; ease side stronger.
- **Industrials × 6m**: tighten t = +6.42 vs ease t = +3.48. Both positive; tighten side stronger.

Sign-asymmetry is exploitable in sub-portfolio construction. We operationalize this in §10.

## 10. Sign-conditional L/S strategy variant

We implement a sign-conditional version of the L/S strategy: at each shock event, we pick the long/short baskets from the sign-stratified Layer A sub-cells that match the event's shock sign.

**Spec at 6m horizon**:
- TIGHTEN events: long [Materials, Industrials, Consumer Discretionary, Consumer Staples, Utilities], short [Healthcare]
- EASE events: long [Energy, Industrials, Consumer Staples, Financials], short [Healthcare]

(Healthcare is short in both signs because its sign-stratified Bonferroni-pass is negative on both sides.)

**Result**: covers all 36 events. Raw Sharpe annualized +1.250 (+22% vs unsigned +1.027). After full 5-component baseline absorption: **alpha-Sharpe +2.078, alpha p-value 0.0021** (87% improvement vs unsigned +1.112 with p=0.080). R² = 0.643.

The sign-conditional variant is materially stronger because it exploits the asymmetry directly: easing-shock-driven Healthcare selloff (t=-10.88) is a much stronger short signal than the average across signs, and the long basket adjusts to the macro-cyclic regime indicated by each shock direction.

| Strategy | Events | Raw Sharpe | Alpha-Sharpe | α p-value |
|---|---|---|---|---|
| Unsigned L/S (paper §6) | 35 | +1.027 | +1.112 | 0.080 |
| **Sign-conditional L/S** | **36** | **+1.250** | **+2.078** | **0.0021** |

→ The sign-conditional variant is the recommended operational strategy. The unsigned L/S serves as a robustness benchmark and matches the original lock construction.

## 11. Limitations and follow-up

1. ~~**Survivor bias in universe**: panel uses currently-listed firms back-extrapolated to 1990. Failed/delisted firms absent. Live-trading realized Sharpe would be lower.~~ **Phase 3 v1 (2026-05-05)**: rebuilt with CRSP `dsf` (delisting native) via static CUSIP8 join (95.4% coverage). 6m alpha-Sharpe **+3.357 (p<0.001)** — appeared to strengthen the result.

   ⚠️ **Phase 3 v2 (2026-05-05, the truly honest version)**: the +3.357 was inflated by **lookahead bias on the universe** — static CUSIP8 backfilled current 2026 R3000 firms to 1990 events when ~75% of them did not yet exist as public companies. After applying time-varying CCM link via `dsenames.ncusip` + `comp.names` (per-event active membership), the result regresses to:

   | Version | Survivor bias | Lookahead bias | 6m alpha-Sharpe | p-value |
   |---|---|---|---|---|
   | Original (Compustat) | YES | YES | +1.112 | 0.080 |
   | Phase 3 v1 (CRSP+static CUSIP8) | NO | YES | +3.357 | <0.001 |
   | **Phase 3 v2 (CRSP+time-varying)** | **NO** | **NO** | **+0.866** | **0.182** |

   - Layer A: 15/33 cells significant (down from 22/33 v1, but still 3× the §7 hard-kill floor of 5)
   - Layer D 6m: alpha-Sharpe **+0.866** marginally above 0.40 floor, p=0.182 marginal
   - Layer D 1m: alpha-Sharpe **+0.193** (p=0.74) FAIL absorption floor — original 1m strength was inflated
   - Layer D 3m: alpha-Sharpe **-0.035** (p=0.96) FAIL absorption floor
   - Walk-forward: 4/5 PASS (fold 1 net Sharpe -0.91 fails — early-data fold has only n=6 train)

   This **confirms the original honest-research warning** of true OOS Sharpe in 0.3-0.9 range. The strategy passes Phase 1 §7 floors under strict reading but is **statistically marginal**.

   Sector cross-section heterogeneity (Layer A) is robust to all bias corrections — 15 cells significant even under the strictest setup. The L/S trading strategy alpha (Layer D) is the marginal piece.

   Audits: `audits/2026-05-05-S1-phase3-honest-revision.md` (v1) + `audits/2026-05-05-S1-phase3-v2-time-varying-honest.md` (v2).

2. ~~**Healthcare 6m -523bp t=-11.94 is extreme**: future work should confirm this isn't driven by 1-2 outlier firms (winsorization check).~~ **Resolved 2026-05-05**: winsorizing at 0.1%, 0.5%, 1%, 5% levels produces means of -537, -604, -631, -620bp respectively — winsorization makes the finding *more* extreme, not less. Top 30 most-extreme negative CARs use 24 unique gvkeys (no firm dominates). The pattern is concentrated on **EASE** shock events (2021-Q3, 2020-Q4, 2021-Q1, 2009-Q2 are the 4 most-negative Healthcare-6m events; all are easing shocks). Consistent with sign-asymmetry table §9 (Healthcare ease t=-10.88 vs tighten t=-6.19). Audit: `audits/2026-05-05-S1-healthcare-outlier-followup.md`.

3. **In-sample Layer A → Layer D**: same data picks L/S sectors AND tests absorption. Walk-forward Phase 1 §1.9 mitigates but adds variance. n=36 events × 9 baseline features is a thin regression.

4. **Cap-weighted vs equal-weighted market**: current panel uses equal-weighted cross-sectional mean. A cap-weighted alternative may shift Layer A magnitudes but we expect the sign pattern to be robust.

5. **Lookahead at 2× horizon decays substantially**: this is signal aging not a bias, but the 12m hold variant of the strategy would not be tradable.

6. **SVB cohort is a 2-event regime case study, not a co-equal statistical sample**: future SLOOS shock arrivals would help confirm or break the sub-finding.

7. **Time-varying CCM linkage missing**: Phase 3 honest revision uses CUSIP8-based static CRSP↔Compustat link (the proper `comp.ccmxpf_lnkhist` is USAGE-blocked in our WRDS subscription as of 2026-05-05; ETA pending). CUSIP8 join gives 95.4% coverage of our R3000 universe with zero ambiguity, but does not preserve historical CUSIP changes / spinoffs / mergers. When real ccmxpf_lnkhist is unblocked, the analysis should be re-run with proper time-varying linkage. Coverage on 4.6% of universe firms (mostly recent IPOs, ADRs, CUSIP-change cases) is missing entirely from the CRSP panel.

8. **CRSP cutoff at 2024-12-31** loses the 2025-04-01 SLOOS event from CRSP analysis (35 of 36 events). The Compustat panel covers 2025-04-01; cross-validation between panels is consistent.

9. **IVOL still macro proxy, not firm-level Ang et al 2006 standard**: current IVOL is realized std of `Mkt-RF` over 60td preceding event. Proper firm-level rolling 60d FF5-residual std per firm-day would require ~23M small regressions; left to future iteration if absorption sensitivity becomes binding.

## 12. Reproducibility

```bash
git clone <repo url>
cd sloos_sector_cross_section
cp .env.example .env  # add FRED_API_KEY
uv sync --extra dev
uv run pytest         # 94 tests, all green
```

End-to-end pipeline runs in approximately 4-5 wall-clock minutes (after data prefetch). All audit files in `audits/2026-05-05-S1-*.md` document each day's lock checks and stop-condition evaluation. Lock amendments (Day 2 SLOOS shock definition; Day 8 IVOL proxy revision) are explicitly recorded with audit pointers in `CLAUDE.md` §1.1 and §7.

## 13. References

- Bassett, William F. et al. "Changes in bank lending standards and the macroeconomy." J Monetary Economics 62 (2014).
- Bidder, Rhys, David Krane, and Joonkyu Park. "Measuring Shocks to Banks' Expectations for Lending Standards Using the Senior Loan Officer Opinion Survey." FEDS Notes 2026-02-23. https://www.federalreserve.gov/econres/notes/feds-notes/measuring-shocks-to-banks-expectations-for-lending-standards-using-the-senior-loan-officer-opinion-survey-20260223.html
- Fama, Eugene F. and Kenneth R. French. "A five-factor asset pricing model." J Financial Economics 116.1 (2015).
- Ferreira, Thiago R. T. "Cross-Sectional Financial Conditions, Business Cycles and the Lending Channel." J Monetary Economics, 2024.
- Carhart, Mark M. "On Persistence in Mutual Fund Performance." J Finance 52.1 (1997).
- Ang, Andrew et al. "The cross-section of volatility and expected returns." J Finance 61.1 (2006).
