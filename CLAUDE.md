# sloos_sector_cross_section (S1)

**Status**: ✅ **LAYER A LOCKED — event-study class** (Gate N thin-event-study class first instance, portfolio second LAYER A LOCKED instance after F6, Macro/Credit pod first LOCKED). Closed 2026-05-05. **한국어 distill**: [analysis/README_KR.md](analysis/README_KR.md).
**Headline result**: Bonferroni-K=33 cell-level **15/33 cells significant** (3× floor) on v3 honest panel; F-test sector heterogeneity 6m **p=1.8e-56**; DRTSCIS alternative event def Spearman **0.83-0.89**; Layer D Δ Sharpe +0.866 (illustrative supplementary).
**Governance close**: `D:/vscode/meta-harness/audits/2026-05-05-S1-governance-close-layer-a-locked-event-study.md` — 5 lock amendment governance-OK with Gate N retroactive legitimization (cell-level event-study PRIMARY 가 Lucca-Moench 2015 / Savor-Wilson 2014 / BKP 2026.02 / Bassett 2014 / Ferreira 2024 prior literature 표준).

**FRAMING (amended 2026-05-05 Phase 4)**: this study is an **event-study regime-detection finding**, not a tradable factor strategy. The headline test is cell-level Bonferroni-corrected significance of sector cross-section heterogeneity post-SLOOS shock; tradable-strategy metrics (Δ Sharpe, walk-forward, net-of-cost) are demoted to robustness sub-checks. Reframing rationale: with n=35 events at quarterly frequency, continuous-trading metrics are under-powered; the canonical event-study literature (Mitchell-Stafford 2000, Lucca-Moench 2015, Savor-Wilson 2014) uses cell-level t-tests + bootstrap CI + sub-period stability + alternative event definitions + regime stratification as the standard validation procedure. Audit: `audits/2026-05-05-S1-phase4-framing.md`.

Fed Senior Loan Officer Opinion Survey (SLOOS) C&I lending standard tightening shock event (분기별 발표 시점) → forward {1mo, 3mo, 6mo} 11 GICS sector cross-section CAR cyclical heterogeneity. Pod: Macro/Credit pod first **LOCKED** (V1 vol pod 와 sub-pod 다름 — vol = market-implied IV term structure, S1 = bank-side credit supply survey). Bonferroni-K=33 strict cell-level test (PRIMARY) + multiple robustness tests (sub-period, bootstrap, alternative event def, regime stratification) + post-2023.Q3 SVB shock cohort sub-sample narrow novel.

## 1. 강제 규칙 (QR Scout discovery)

1. **SLOOS shock 정의 lock (amended 2026-05-05 Day 2)** — primary `DRTSCILM` (FRED Net % C&I tightening Large/Middle-Market) 에 full-sample **AR(1) fit → residual ε_t** 추출 → `z_innov = ε_t / σ(ε)` 표준화 → `|z_innov| > 1.0σ` quarter 가 shock event. Sign: tightening (+) if ε_t>0, easing (−) otherwise. AR(1)-residual 은 by construction 약 white noise 이므로 first-quarter cluster filter 불필요. **Amendment 사유**: 원래 "rolling 40q level z-score >1.5σ first-quarter event" 정의는 SLOOS series 의 3-regime 구조 (early-2000s / GFC / COVID+post-COVID) + AR(1) ρ≈0.86 high persistence 때문에 strict 적용 시 events=5 (§7 floor 30 미달). AR-innovation 정의는 Bidder-Krane-Park 2026.02 E-CSI methodology 의 standard 이며 persistence 를 방어한다. 1.0σ threshold 는 AR-innovation 표준 (Bassett 2014, Bidder-Krane-Park 2026.02); 원래 1.5σ 는 level-z 용. Calibration: AR(1) ρ=0.86, σ(ε)=11.24, events=36 (19T / 17E), SVB cohort=2. Audit pointer: `audits/2026-05-05-S1-day2-eod.md`. 변경 시 추가 audit 의무.
2. **Universe lock** — R3000 mapped to GICS 11 sectors via Compustat secd × `comp.security` × `comp.company.gsector`. R3000 holdings public CSV (iShares IWB/IWN/IWM) + GVKEY 매핑.
3. **Forward horizons + cell-level test (PRIMARY) lock** — {1mo, 3mo, 6mo}. Bonferroni-K = 11 sectors × 3 horizons = **33**, critical t ≈ **3.17** (df-finite) 양측 α=0.05. **PRIMARY headline metric (Phase 4 amendment)**: ≥5 cells significant at Bonferroni-K=33 → sector cross-section heterogeneity established.
4. **F1-1 minority-class n_min** — per (sector × horizon) cell n_with_CAR ≥ **50 events** (live-trading floor strict). Expected ~9,450 firm-events per cell ≫ 50.
5. **F6 escape mechanism 4 의무** — event=SLOOS quarterly release ✓ / 11 GICS sectors pre-strat ✓ / minority n ≥ 50 ✓ / SLOOS baseline-외 component (FF5/Mom/IVOL/SRF/E-CSI 5종 distinct).
6. **Layer D 5-component baseline lock** — **FF5 + Mom + IVOL + SRF (Ferreira 2024 cross-section financial firm skewness 재구축) + E-CSI proxy (Fed 2026.02 Bidder-Krane-Park SLOOS shock methodology 재구축)**. Day 5 commit hash 안 박힘.
7. **F6 absorption gate Δ Sharpe ≥ 0.40** (Phase 4 demoted to **robustness sub-check**, not headline gate) — under event-study framing, Sharpe-based metric is illustrative only. Original lock kept for compatibility but no longer binds outcome class. Audit: `audits/2026-05-05-S1-phase4-framing.md`.
8. **Layer A vs Layer D 분리 보고** — F1-6 inheritance. mechanism PASS / tradability FAIL 가 valid frozen-two-layer.
9. **Walk-forward** (Phase 4 demoted to robustness) — 5-fold chronological 80/20 split, ≥ 4/5 fold positive net-cost Sharpe. Phase 4 framing: tradable-strategy stability check, not headline.
10. **Gate L lookahead shift sweep** (Phase 4 demoted) — original Phase 1 §1.7 metric. Under event-study framing, lookahead is intrinsic to event-window definition (we already use t0=event-date, fixed horizons).
11. **Gate K multi-year sub-period reproduction (PRIMARY robustness test)** — 1990-2010 (pre-GFC) vs 2010-2026 (post-GFC) **cell-level pattern correlation ≥ 0.5** (Phase 4 amendment: was Sharpe ratio). + post-2023.Q3 SVB cohort sub-sample 단독 (case study, not co-equal).
12. **Gate M net-of-cost** (Phase 4 demoted to illustrative) — for trading deployment if reframed as factor; not a regime-detection gate.

**Phase 4 PRIMARY robustness tests (added 2026-05-05)**:
- **(a) F-test sector heterogeneity**: one-way ANOVA across 11 sectors per horizon, p<0.05 obligatory at ≥1 horizon
- **(b) Bootstrap CI on cell t-stats**: 1,000 event-level resampling iterations; ≥5 cells with 90% CI lower-bound > Bonferroni critical 3.17
- **(c) Alternative event definition**: DRTSCIS-derived events (small-firm SLOOS) → cell-level Spearman correlation with primary DRTSCILM ≥ 0.5
- **(d) VIX-regime stratification**: high-VIX vs low-VIX events; sector pattern direction preserved (sign agreement ≥ 7/11)
13. **Phase 0 #8 Product-market trigger 강화** — weekly Fed FEDS Notes / NBER / arXiv q-fin / SSRN finance monitor (Day 1 + 7 + 12 자동 search). "SLOOS shock × cross-section equity sector" 또는 유사 paper 출현 시 즉시 freeze. **Fed scoop risk 30-50%** (Bidder-Krane-Park 2026.02 follow-up risk).
14. **LLM-light cap=$5** — `shared_utils.openrouter_client(project="sloos_sector_cross_section" cap=$5)`. scoop re-check Day 1+7+12 only. Numeric 위주 paper.
15. **Karpathy 4원칙** + drift-watchdog 매 phase + abandon-criteria 매 phase + karpathy-guidelines 신규 task + protected-long-task (없는 듯, FRED API call <50).
16. **Tests 의무** — 모듈마다 unit test, total ≥ 35 tests Day 14 까지. uv-pytest.
17. **Resume harness** — atomic_write + manifest checkpoint 매 step. WRDS courier query + FRED API call manifest 누적.

## 2. 데이터 sources

- **SLOOS primary**: FRED `DRTSCILM` (1990.Q1+, 140+ quarters)
- **SLOOS robust**: FRED `DRTSCIS` / `DRTSCRE` / `DRTSRRE` / `DRTSCC` / `DRTSAUTO` (sensitivity check)
- **Fed SLOOS PDF**: https://www.federalreserve.gov/data/sloos.htm 분기 PDF parser sanity (Phase 0 Day 1)
- **Compustat secd** (WRDS courier): `comp_na_daily_all.secd` 1.4GB GVKEY+IID daily
- **GICS mapping**: `comp.company.gsector` (11 sectors)
- **R3000 universe**: iShares IWB/IWN/IWM holdings public CSV + ticker → GVKEY via `comp.security`
- **FF5 + Mom**: Ken French data library public CSV
- **IVOL**: 자체 계산 (60d rolling FF5 residual std)
- **SRF (Ferreira 2024)**: 자체 재구축 (Compustat secd 안 financial sector cross-section skewness)
- **E-CSI proxy (Fed 2026.02)**: 자체 재구축 (Bidder-Krane-Park methodology — SLOOS aggregate 기반 proxy)

## 3. Project type / Pod

- **Project type**: discovery (alpha-research). Gate G v1.2 lock.
- **Pod**: Macro/Credit pod first (portfolio empty pod 채움). V1 vol pod 와 sub-pod 다름.
- **Daemon-free**: ✓ (FRED API REST polling, no daemon)
- **Sample-window**: 1990.Q1-2026.Q1 primary (~140 quarters) + post-2023.Q3 SVB cohort sub-sample.

## 4. Phase 0/1/2 plan (14d hard cap)

| Day | Task | Trigger / Gate |
|---|---|---|
| 1 | WRDS courier verify + FRED `DRTSCILM` fetch + R3000 universe + GICS map + scoop re-check #1 | Phase 0 #1, #2, #8 |
| 2 | Robust SLOOS series + Fed PDF parser + shock_construct.py + EDA event count | #3, #4, #6 |
| 3 | sector_panel build + per-cell n_min audit + Phase 0 EOD audit | #5, P1 |
| 4-5 | layer_a.py + Bonferroni-33 critical | Phase 1 #1 setup |
| 6-7 | srf_construct.py (Ferreira 2024) + ecsi_construct.py (Fed 2026.02) | 5-component baseline build |
| 8-9 | layer_d.py 5-component absorb + Δ Sharpe + Gate M sanity | Phase 1 #3 |
| 10 | gate_l_shift_sweep.py + gate_k_subperiod.py | Phase 2 #1, #2 |
| 11 | walk_forward.py 5-fold + scoop re-check #2 | Phase 2 #3 |
| 12 | Phase 1+2 mid-checkpoint + SVB cohort sub-finding 분석 | P2 |
| 13 | outcome decision (LAYER A LOCKED / frozen-two-layer / ABANDONED) | P2 |
| 14 | paper_v1 draft + dashboard + bilingual README + status file (LAYER_A_LOCKED.md / FROZEN_TWO_LAYER.md / ABANDONED.md) + scoop #3 → **STOP, no gh push from S1** (governance review at meta-harness) | hard cap |

## 5. Outcome class (QR Scout discovery)

S1 안에서는 **status file + draft artifacts 까지만** 작성. **GitHub push 는 본 repo 안 직접 수행 X** — Day 14 후 사용자가 meta-harness 로 복귀, governance review 후 meta-harness 에서 gh push 결정/실행.

**Phase 4 amended outcome class** (event-study regime detection framework):

- **REGIME DETECTION FINDING ESTABLISHED** (formerly LAYER A LOCKED): Layer A cell-level ≥5 + ≥3 of 4 Phase 4 PRIMARY robustness tests PASS → `LAYER_A_LOCKED.md` + paper draft + dashboard + bilingual README → **STOP** → meta-harness governance review
- **borderline-finding** (formerly frozen-two-layer): Layer A cell-level PASS but ≤2 of 4 Phase 4 PRIMARY robustness tests PASS → `FROZEN_TWO_LAYER.md` + caveats; the headline cell-level finding may still be publishable as discovery note with explicit boundaries
- **REJECTED** (formerly ABANDONED): Layer A cell-level FAIL (<5 cells significant) → `ABANDONED.md`
- **Fed scoop trigger**: weekly monitor → 14d 안 freeze 가능 → STOP → meta-harness review

Legacy Sharpe-based gates (§1.7 §1.9 §1.10 §1.12) are reported as supplementary metrics in paper §13 but do not bind outcome class under Phase 4 framing.

## 6. Bayesian prior + 6th frozen 회피

- post-informed_flow: frozen-two-layer 5/11=45.5%, LAYER A LOCKED 1/11=9.1%
- S1 best LAYER A LOCKED ~25-30% (F6 escape 4-of-4 partial fit)
- S1 mid frozen-two-layer ~40-45%
- S1 worst ABANDONED ~15-20%
- S1 Fed scoop trigger ~20-30% (weekly monitor 통과 못할 시)

**6th frozen 회피 lever 4종**:
1. 5-component baseline 분리 보고 (각 component 별 incremental Δ Sharpe)
2. Sector × horizon 33 strata 분리 보고 (cyclical-only sub-portfolio)
3. SVB cohort sub-sample 분리 보고 (regime-conditional finding)
4. Sign asymmetry (tightening vs easing shock 부호별)

## 7. Abandon Triggers (4-cat 각 ≥ 1)

(Full list: D:/vscode/meta-harness/audits/2026-05-05-S1-sloos-reference-validation.md §4)

- **Data-validity**: WRDS/FRED fail / DRTSCILM <140q / events <30 / SVB cohort <1 (amended 2026-05-05 Day 2: original ≥8 floor unreachable under any threshold given only ~11 SVB-cohort release dates exist 2023.Q3-2026.Q2; SVB sub-finding now §6 lever-3 regime case study not co-equal statistical sample) / per-cell n <50
- **Mechanism**: Layer A Bonferroni-33 PASS <5 / Layer D Δ Sharpe <0.4 / Gate L decay <0.5 / Gate K subperiod <0.5 / Gate M net-Sharpe <0 / Walk-forward <4/5 / over-concentration top-3 sector >70%
- **Resource**: OpenRouter >$5 / Day 14 hard cap
- **Product-market 강화**: weekly Fed FEDS / NBER / arXiv 새 paper 출현 시 즉시 freeze

## 8. 강제 인프라 활용 (Gate E)

- `shared_utils.atomic_io.atomic_write_json + FileLock`
- `shared_utils.openrouter_client(project="sloos_sector_cross_section" cap=$5)`
- `shared_utils.rigor_checks` (DSR + BH-FDR + cluster bootstrap + Newey-West HAC)
- `shared_utils.locks_check` (locks_registry.yaml verify)
- WRDS courier `wrds_courier_client.open_db()` + `query()` (Read(E:/wrds-data-courier/**) settings.json allow)
- skills: karpathy-guidelines / drift-watchdog / abandon-criteria / repo-autonomy-overnight

## 9. 비대상

- Live-trading deployment (S1 = QR Scout discovery, NOT live-trading-research)
- Aggregate macro analysis (Bassett 2014 territory) — S1 = sector-decomposed 11 GICS strict
- Inverse direction (cross-section returns → lending channel barometer, Ferreira 2024 territory) — S1 = forward direction (SLOOS → returns)
- E-CSI lending standard prediction (Fed 2026.02 Bidder-Krane-Park) — S1 = equity sector forward CAR target
- **GitHub public push 본 repo 안 직접 수행 금지** (2026-05-05 governance lock retro-fix) — Day 14 outcome 후 사용자 meta-harness 복귀, governance review 통과 후 meta-harness 에서 gh push 실행
- **OpenRouter API key 본 repo `.env` 명시 금지** (2026-05-05 governance lock retro-fix) — portfolio-coordination 중앙 config 가 `shared_utils.openrouter_client` 통해 처리

## 10. 참고 audit

- **Comprehensive research report (Phase 0-4 종합 + governance review용)**: `D:/vscode/meta-harness/audits/2026-05-05-sloos_sector_cross_section-comprehensive-research-report.md` (~985 lines, 19 sections + 4 appendices)
- reference validation: `D:/vscode/meta-harness/audits/2026-05-05-S1-sloos-reference-validation.md` (~700 lines)
- launch overnight prompt: `D:/vscode/meta-harness/audits/2026-05-05-S1-overnight-start-prompt.md`
- settings.json template: `D:/vscode/meta-harness/audits/2026-05-05-S1-settings.json.template.md`
- portfolio-research-rules §3 row: `D:/vscode/meta-harness/docs/portfolio-research-rules.md`
- F1 lessons: `D:/vscode/meta-harness/audits/2026-04-27-fda-adcomm-frozen-postmortem.md`
- F6 escape mechanism: `D:/vscode/meta-harness/audits/2026-04-28-clinicaltrials-amendment-f6-layer-a-locked-reception.md`
- Gate K/L/M (informed_flow inheritance): `D:/vscode/meta-harness/audits/2026-05-04-informed-flow-crypto-perp-retraction.md`
- WRDS courier: `E:\wrds-data-courier\INTERFACE.md`
- S1 daily/phase audits (17 files): `audits/2026-05-05-S1-*.md` — bootstrap, day1/2/3/5/7/9/10/11/14, phase0/3/3v2/4-framing/4-eod, sign-conditional, healthcare-outlier, courier-followup
