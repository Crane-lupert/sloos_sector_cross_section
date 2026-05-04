# sloos_sector_cross_section (S1)

Fed Senior Loan Officer Opinion Survey (SLOOS) C&I lending standard tightening shock event (분기별 발표 시점) → forward {1mo, 3mo, 6mo} 11 GICS sector cross-section CAR cyclical heterogeneity. Pod: Macro/Credit pod first (V1 vol pod 와 sub-pod 다름 — vol = market-implied IV term structure, S1 = bank-side credit supply survey). Bonferroni-K=33 strict + post-2023.Q3 SVB shock cohort sub-sample narrow novel. Layer D 5-component baseline absorb 의무.

## 1. 강제 규칙 (QR Scout discovery)

1. **SLOOS shock 정의 lock (amended 2026-05-05 Day 2)** — primary `DRTSCILM` (FRED Net % C&I tightening Large/Middle-Market) 에 full-sample **AR(1) fit → residual ε_t** 추출 → `z_innov = ε_t / σ(ε)` 표준화 → `|z_innov| > 1.0σ` quarter 가 shock event. Sign: tightening (+) if ε_t>0, easing (−) otherwise. AR(1)-residual 은 by construction 약 white noise 이므로 first-quarter cluster filter 불필요. **Amendment 사유**: 원래 "rolling 40q level z-score >1.5σ first-quarter event" 정의는 SLOOS series 의 3-regime 구조 (early-2000s / GFC / COVID+post-COVID) + AR(1) ρ≈0.86 high persistence 때문에 strict 적용 시 events=5 (§7 floor 30 미달). AR-innovation 정의는 Bidder-Krane-Park 2026.02 E-CSI methodology 의 standard 이며 persistence 를 방어한다. 1.0σ threshold 는 AR-innovation 표준 (Bassett 2014, Bidder-Krane-Park 2026.02); 원래 1.5σ 는 level-z 용. Calibration: AR(1) ρ=0.86, σ(ε)=11.24, events=36 (19T / 17E), SVB cohort=2. Audit pointer: `audits/2026-05-05-S1-day2-eod.md`. 변경 시 추가 audit 의무.
2. **Universe lock** — R3000 mapped to GICS 11 sectors via Compustat secd × `comp.security` × `comp.company.gsector`. R3000 holdings public CSV (iShares IWB/IWN/IWM) + GVKEY 매핑.
3. **Forward horizons lock** — {1mo, 3mo, 6mo}. Bonferroni-K = 11 sectors × 3 horizons = **33**, critical t ≈ **3.04** 양측 α=0.05.
4. **F1-1 minority-class n_min** — per (sector × horizon) cell n_with_CAR ≥ **50 events** (live-trading floor strict). Expected ~9,450 firm-events per cell ≫ 50.
5. **F6 escape mechanism 4 의무** — event=SLOOS quarterly release ✓ / 11 GICS sectors pre-strat ✓ / minority n ≥ 50 ✓ / SLOOS baseline-외 component (FF5/Mom/IVOL/SRF/E-CSI 5종 distinct).
6. **Layer D 5-component baseline lock** — **FF5 + Mom + IVOL + SRF (Ferreira 2024 cross-section financial firm skewness 재구축) + E-CSI proxy (Fed 2026.02 Bidder-Krane-Park SLOOS shock methodology 재구축)**. Day 5 commit hash 안 박힘.
7. **F6 absorption gate Δ Sharpe ≥ 0.40** — academic 0.30 보다 강 (Fed 2024-2026 active 영역 differentiation).
8. **Layer A vs Layer D 분리 보고** — F1-6 inheritance. mechanism PASS / tradability FAIL 가 valid frozen-two-layer.
9. **Walk-forward 의무** — 5-fold chronological 80/20 split, ≥ 4/5 fold positive net-cost Sharpe.
10. **Gate L lookahead shift sweep** — shift = 1 → 2×forward_horizon (1mo→2mo, 3mo→6mo, 6mo→12mo). Sharpe ratio decay ≥ 0.5 PASS. < 0.5 시 honest shift(forward_horizon+1) 재산출.
11. **Gate K multi-year sub-period reproduction** — 1990-2010 (pre-GFC) vs 2010-2026 (post-GFC) Sharpe ratio ≥ 0.5 의무. + post-2023.Q3 SVB cohort sub-sample 단독 ≥ 0.5 of full.
12. **Gate M net-of-cost** — 6mo hold sector ETF ~5bp roundtrip × turnover ~0.5/yr = ~5bp/yr cost (low cost regime). net-Sharpe ≥ 0 obligatory.
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
| 14 | paper_v1 + dashboard + bilingual README + GitHub push (LAYER A LOCKED 시) + scoop #3 | hard cap |

## 5. Outcome class (QR Scout discovery)

- **LAYER A LOCKED**: Layer A + Layer D + Walk-forward 3-of-3 PASS → paper + Streamlit + bilingual README + GitHub public push
- **frozen-two-layer**: Layer A PASS + Layer D FAIL → 6th frozen-two-layer instance, post-mortem-negative-result-template, reports/postmortems/. SVB cohort sub-finding standalone publishable
- **ABANDONED**: Layer A FAIL → ABANDONED.md
- **Fed scoop trigger**: weekly monitor → 14d 안 freeze 가능

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

## 10. 참고 audit

- reference validation: `D:/vscode/meta-harness/audits/2026-05-05-S1-sloos-reference-validation.md` (~700 lines)
- launch overnight prompt: `D:/vscode/meta-harness/audits/2026-05-05-S1-overnight-start-prompt.md`
- settings.json template: `D:/vscode/meta-harness/audits/2026-05-05-S1-settings.json.template.md`
- portfolio-research-rules §3 row: `D:/vscode/meta-harness/docs/portfolio-research-rules.md`
- F1 lessons: `D:/vscode/meta-harness/audits/2026-04-27-fda-adcomm-frozen-postmortem.md`
- F6 escape mechanism: `D:/vscode/meta-harness/audits/2026-04-28-clinicaltrials-amendment-f6-layer-a-locked-reception.md`
- Gate K/L/M (informed_flow inheritance): `D:/vscode/meta-harness/audits/2026-05-04-informed-flow-crypto-perp-retraction.md`
- WRDS courier: `E:\wrds-data-courier\INTERFACE.md`
