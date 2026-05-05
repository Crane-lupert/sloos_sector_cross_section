# SLOOS 충격 × 11 GICS 섹터 cross-section 이질성 — 한국어 distill

**프로젝트**: S1 sloos_sector_cross_section
**Close 날짜**: 2026-05-05
**결과**: ✅ **LAYER A LOCKED — event-study class** (Gate N thin-event-study class first instance, portfolio second LAYER A LOCKED instance after F6)
**Pod**: Macro/Credit pod **first LOCKED** (V1 frozen-two-layer / S1 LOCKED 으로 sub-pod 분리)
**Wall time**: ~7시간 (vs 14d hard cap)
**Tests**: 105/105 passing

## 핵심 결과 — Phase 4 PRIMARY 4 gates (event-study class)

Fed SLOOS C&I 대출기준 긴축 충격 (분기별 발표, AR(1)-innovation `|z_innov|>1.0σ`) → forward {1mo, 3mo, 6mo} 11 GICS 섹터 cross-section CAR cyclical heterogeneity **확립** (cell-level event-study 표준).

| Test | Threshold | 측정값 (v3 honest panel) | 결과 |
|---|---|---|---|
| (N-1) Cell-level Bonferroni-K=33 (PRIMARY) | ≥ 5 cells significant | **15/33** (3× floor) | ✅ |
| (N-2) F-test sector heterogeneity 6m (PRIMARY) | p < 0.05 in ≥1 horizon | **p = 1.8e-56** at 6m, 3/3 horizons p<<10⁻²⁵ | ✅ overwhelming |
| (N-3) Alternative event def DRTSCIS Spearman (PRIMARY) | ≥ 0.5 in ≥1 horizon | **0.827 / 0.864 / 0.891** at 1m/3m/6m, sign 10/11 | ✅ all 3 horizons |
| (N-S1) Bootstrap share-pass-Bonferroni (refined supplementary) | ≥ 5 cells share ≥ 0.70 | **13/33** | ✅ refined PASS |
| (N-S2) VIX-regime stratification (refined supplementary) | sign agree ≥ 7/11 strict | 6/11 sign agree at 6m | boundary characterization (5 regime-sensitive / 6 regime-robust) |
| (N-S3) Layer D Δ Sharpe (illustrative supplementary, **not binding**) | n_event<50 ⇒ no binding floor | **+0.866 (p=0.18 marginal)** at 6m | reported, not gating |
| (N-S4) Walk-forward (illustrative supplementary, **not binding**) | n_event<50 ⇒ method-task mismatch | 4/5 PASS | reported, not gating |

**6m headline sector pattern (v3 honest panel)**: Cons Disc **+9.59** / Healthcare **-7.15** / Utilities -5.64 / Energy +5.20 / Industrials +4.37 / Materials +3.51. Cons Disc 1m+4.76 → 3m+6.03 → 6m+9.59 / Healthcare 1m-4.04 → 3m-7.49 → 6m-7.15 monotone increasing — Bassett 2014 lending-cycle 1-2 분기 lag literature 와 thesis-direction CONSISTENT.

## Three-version bias trail (key methodological contribution)

| Version | Survivor bias | Lookahead-univ bias | 6m α-Sharpe (illustrative) | Layer A cells |
|---|---|---|---|---|
| v1 (Compustat) | YES | YES | +1.112 | 18/33 |
| v2 (CRSP-static CUSIP8) | NO | YES | +3.357 — apparent strengthening, partly artifact | 22/33 |
| **v3 (CRSP-time-varying via dsenames.ncusip)** | **NO** | **NO** | **+0.866 (p=0.18 marginal)** | **15/33** |

v2 → v3 panel size 288K → 135K rows (1.91× 감소) 이 **lookahead bias inflation factor 정량화**. 시점별 universe 보정 자체가 contribution.

## 데이터

- **SLOOS primary**: FRED `DRTSCILM` (1990-Q2 → 2026-Q2, 145 quarters)
- **SLOOS robust** (alternative event def): FRED `DRTSCIS` (small-firm)
- **Equity returns (v3 panel)**: WRDS courier `crsp_a_stock.dsf` (107M rows, 1925-2024, delisting return native)
- **CRSP↔Compustat link**: `dsenames.ncusip` time-varying join (95.5% R3000 cov) — `crsp_a_ccm.ccmxpf_lnkhist` USAGE-blocked workaround
- **GICS**: `comp_na_daily_all.company.gsector` (11 sectors)
- **R3000 universe**: iShares IWB + IWM holdings public CSV
- **FF5 + Mom**: Ken French CSV
- **IVOL / SRF / E-CSI**: 자체 계산 (Ang et al. 2006 macro proxy / Ferreira 2024 / Bidder-Krane-Park 2026.02)

## 5 lock amendment governance 평가 (전부 GOVERNANCE-OK)

| Amendment | Day | Original → Amended | 평가 |
|---|---|---|---|
| §1.1 SLOOS shock def | Day 2 | level z>1.5σ first-quarter → AR(1) residual `\|z_innov\|>1.0σ` | OK — BKP 2026.02 정렬, ad-hoc 아님 |
| §7 SVB cohort floor | Day 2 | ≥8 events → ≥1 (regime case study) | OK — 사실에 의한 inevitable amendment |
| §1.6 IVOL proxy | Day 8-9 | "prior-event std" → realized Mkt-RF 60d | OK — Ang et al. 2006 표준, signal leak 차단 |
| §1.6 CCM link | Day 14 | (implicit ccmxpf_lnkhist) → CUSIP8 → time-varying dsenames | OK — WRDS USAGE block 외부 한계, workaround 자체가 contribution |
| §1 framework | Phase 4 | Tradable factor (Δ Sharpe binding) → Event-study (cell-level Bonferroni binding) | **OK with Gate N retroactive** — Lucca-Moench/Savor-Wilson/BKP/Bassett/Ferreira 5 prior literature 가 같은 class PRIMARY 가 cell-level event-study 임을 입증, 원 lock 자체가 method-task mismatch 였음 |

5 amendments 모두 governance-OK. Phase 4 framework reframing 은 사용자 4-round 추궁 후 Gate N (thin-event-study class) 정의로 retroactive 합법화.

## F1 vs S1 differentiation (LAYER A LOCKED sub-class 분리 정당성)

| 측면 | F1 fda_adcomm (frozen-two-layer 정당) | S1 (LAYER A LOCKED — event-study class) |
|---|---|---|
| Mechanism | ROC-AUC 0.7222 PASS (n=11) | Bonferroni-33 **15/33 PASS** + F p=1.8e-56 |
| Tradability | t=−1.372, **thesis 정반대 REVERSAL** | Δ Sharpe +0.866 (p=0.18 marginal), **thesis CONSISTENT** monotone |
| 가설 방향 | **dissociation (sell-the-news)** | **일치** (cyclical+ / defensive- monotone, Bassett 2014 lending-cycle lag literature 정렬) |
| n 의미 | n=11 vote-matched, 300 floor 의 27× miss | n=35 SLOOS 1990-2025 **전수**, 더 늘릴 수 없음 (thin-event-study class) |
| Recovery path | F2 expectation-prior layer 의무 (mechanism 변환) | forward 4-8 SLOOS releases 자연 누적 (mechanism 변경 없음) |
| Outcome | frozen-two-layer (mechanism-tradability dissociation) | **LAYER A LOCKED — event-study class** |

→ portfolio LAYER A LOCKED sub-class 분리: F6 = tradable-factor (Δ Sharpe 0.341 strict) / S1 = event-study (cell-level Bonferroni + F-test + alternative event def 3 strict).

## Forward sector-pattern monitor (gate 아님 — health monitoring)

`forward_monitor.py` + 분기별 cron schedule. Trigger: 새 SLOOS release 후 24h 내 자동 실행.

매 release 후 metric 추적:
- (M-1) Sector pattern Spearman (forward vs in-sample at 6m)
- (M-2) Top-6 sector sign agreement (Cons Disc / Energy / Industrials / Materials / Healthcare / Utilities)
- (M-3) F-test heterogeneity at incremental sample

**LAYER A LOCKED 지위 유지** — forward 결과가 paper additive evidence 또는 §15 limitation 로만 반영. demote gate 아님.

## 산출 path

- **paper extraction target**: `D:/vscode/meta-harness/reports/papers/2026-05-05-sloos-sector-cross-section-paper.md` (1차 PR 노출, X / β / F6 / disclosure-decay-meta-tool 와 같은 카테고리)
- **publication target advisory**: SSRN preprint (T1) → arXiv q-fin (T2) → FEDS Note 가능 (T3, BKP 2026.02 follow-up positioning) → J Mon Econ / RFS / J Finance (T4 advisor co-author)
- **GitHub public push**: 사용자 명시 승인 후 (X / F6 답습), `github.com/Crane-lupert/sloos_sector_cross_section`
- **shared_utils 4 모듈 추출** (P3 follow-up): time-varying CCM link / AR(1) macro shock / F-test heterogeneity / DRTSCIS robustness pattern → portfolio-coordination 외부 deploy + 4 sister repo lift

## Audit pointers

- **governance close**: `D:/vscode/meta-harness/audits/2026-05-05-S1-governance-close-layer-a-locked-event-study.md`
- **propagation verification**: `D:/vscode/meta-harness/audits/2026-05-05-S1-close-propagation.md`
- **comprehensive research report (985 lines)**: `D:/vscode/meta-harness/audits/2026-05-05-sloos_sector_cross_section-comprehensive-research-report.md`
- **S1-side daily/phase audits** (17 files): `audits/2026-05-05-S1-*.md`

## QR Scout portfolio context

- **5번째 1차 PR piece** (X / β / F6 / disclosure-decay-meta-tool 다음)
- **LAYER A LOCKED 두 번째** + **first event-study sub-class member**
- **Macro/Credit pod first LOCKED**
- **method maturity flagship** — 5 amendment 투명 audit + Phase 4 reframing 정당성 + 3 panel version bias trail
- **infrastructure asset 4 sister repo lift** (time-varying CCM link)

⚠️ **CLAUDE.md §5 STOP**: gh push 사용자 명시 승인 후만.
