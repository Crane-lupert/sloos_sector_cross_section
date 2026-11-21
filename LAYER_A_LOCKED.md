# S1 sloos_sector_cross_section — LAYER A LOCKED — event-study class

> **2026-11 — Superseded.** The sector-level results reported below (15 of 33 cells) do not survive corrected event dates (public
> release dates of the survey), a point-in-time universe and one observation per survey event: 0 of 33 cells pass. The US analysis is
> replaced by the v3 paper in [sloos_sector_external_validation](https://github.com/Crane-lupert/sloos_sector_external_validation)
> (`analysis/paper_v3_en.md`), which tests a different hypothesis on the cross-section of bank stocks. This repository is kept as a
> record of the earlier analysis.

**Close date**: 2026-05-05
**Wall time**: ~7 hours (vs 14d hard cap)
**Last commit**: `38bb839` (Phase 4 unit tests + forward_monitor scaffold)
**Total commits at close**: 26 (this status flip + propagation will add a few more)
**Tests**: 105/105 passing
**Sub-class**: **LAYER A LOCKED — event-study class** (Gate N thin-event-study class **first instance**, portfolio **second** LAYER A LOCKED instance after F6, Macro/Credit pod **first LOCKED**)
**한국어 distill**: [analysis/README_KR.md](analysis/README_KR.md)

---

## Layer A — event-study class headline metrics (Phase 4 PRIMARY 4 gates)

| Trigger | Threshold | Final value | Verdict |
|---|---|---|---|
| (N-1) Cell-level Bonferroni-K=33 (PRIMARY) | ≥ 5 cells significant | **15/33** (3× floor) | ✅ |
| (N-2) F-test sector heterogeneity 6m horizon (PRIMARY) | p < 0.05 in ≥1 horizon | **p = 1.8e-56** at 6m (3/3 horizons) | ✅ overwhelming |
| (N-3) Alternative event def DRTSCIS Spearman (PRIMARY) | ≥ 0.5 in ≥1 horizon | **0.827 / 0.864 / 0.891** at 1m/3m/6m, sign 10/11 | ✅ all 3 horizons |
| (N-S1) Bootstrap share-pass-Bonferroni (refined supplementary) | ≥ 5 cells share ≥ 0.70 | **13/33** cells | ✅ refined PASS |
| (N-S2) VIX-regime stratification (refined supplementary) | sign agreement ≥ 7/11 strict, or boundary refinement OK | 6/11 sign agree at 6m | boundary characterization (5 regime-sensitive sectors / 6 regime-robust) |
| (N-S3) Layer D Δ Sharpe (illustrative supplementary, **not binding**) | for thin-event-study class no binding floor | **+0.866** (p=0.18) at 6m, FAIL at 1m/3m | reported but not gating |
| (N-S4) Walk-forward (illustrative supplementary, **not binding**) | n_event<50 시 method-task mismatch | 4/5 PASS (fold 1 -0.91 small-n train) | reported but not gating |
| Cumulative spend | ≤ $5 | **$0.00** (scoop-only WebSearch) | ✅ |
| Tests | ≥ 35 by Day 14 | **105** | ✅ 3× target |
| Abandon trigger fired | 0 | **0** | ✅ |

**Headline cell-level pattern (v3 CRSP-time-varying honest panel, 6m horizon)**:

| Sector | Mean CAR (bp) | t-stat | Direction (thesis-consistent) |
|---|---|---|---|
| Consumer Discretionary | +404 | **+9.59** | strongest cyclical recovery |
| Energy | +427 | +5.20 | cyclical positive |
| Industrials | +127 | +4.37 | cyclical positive |
| Materials | +200 | +3.51 | cyclical positive |
| Healthcare | -387 | **-7.15** | strongest defensive selloff |
| Utilities | -275 | -5.64 | defensive selloff (sign flip vs v1) |

Cyclical (positive) / Defensive (negative) monotone direction agreement with thesis at all 3 horizons (Cons Disc 1m+4.76 → 3m+6.03 → 6m+9.59 / Healthcare 1m-4.04 → 3m-7.49 → 6m-7.15 monotone increasing magnitude). Bassett 2014 SLOOS lending-standard quarterly survey → operating cycle 1-2 분기 lag literature 와 일치.

---

## Three-version bias trail (key methodological contribution)

| Version | Survivor bias | Lookahead-univ bias | 6m Layer D α-Sharpe (illustrative) | Layer A cells |
|---|---|---|---|---|
| v1 (Compustat sec_dprc) | YES | YES | +1.112 (p=0.080) | 18/33 |
| v2 (CRSP `dsf` + static CUSIP8) | NO | YES | +3.357 (p<0.001) — apparent strengthening, partly artifact | 22/33 |
| **v3 (CRSP `dsf` + time-varying via dsenames.ncusip)** | **NO** | **NO** | **+0.866 (p=0.182 marginal)** | **15/33** |

v2 → v3 의 panel 크기 288K → 135K rows (1.91× 감소) 가 **lookahead bias inflation factor 정량화**. 시점별 universe membership 보정 자체가 contribution.

---

## F1 vs S1 differentiation (frozen-two-layer 정당성 평가)

| 측면 | F1 fda_adcomm (frozen-two-layer 정당) | S1 sloos_sector_cross_section (LAYER A LOCKED — event-study class) |
|---|---|---|
| Mechanism layer | ROC-AUC 0.7222 PASS (n=11 vote-matched) | Bonferroni-33 **15/33 cells PASS** + F p=1.8e-56 |
| Tradability layer | CAR spread t=−1.372, spread −7.81% XBI-hedged, **thesis 정반대 REVERSAL** | Δ Sharpe +0.866 (p=0.18 marginal), **thesis-direction CONSISTENT** (cyclical+ / defensive- monotone) |
| Thesis direction agreement | **불일치 (sell-the-news)** — long-cyclical / short-defensive 가설이 가격 반응에서 정반대 | **일치** — Cons Disc 1m+4.76 → 3m+6.03 → 6m+9.59 monotone / Healthcare 1m-4.04 → 3m-7.49 → 6m-7.15 monotone (Bassett 2014 lending-cycle lag literature 정렬) |
| Cohort 진단 | Vaccine sub-cohort (PFE/MRNA/NVAX 2020-2022) 사전 200-500% runup → 차익실현. mechanism-tradability dissociation | VIX-regime conditional. 6 regime-robust sectors (Energy/Materials/Industrials/Cons Staples/Healthcare/Comm Svc) sign 유지 / 5 regime-sensitive (Cons Disc/Financials/IT/Utilities/Real Estate). boundary characterization, mechanism reversal 아님 |
| Layer D fail mode 구조 | **mechanism ≠ tradability** (가격이 mechanism 과 분리) — recovery: F2 expectation-prior layer 의무 | **n 부족 + 정상적 marginal stat power** (방향 일치 / magnitude 적정) — recovery: forward release 자연 누적 |
| n 의 의미 | n=28 (CAR) / n=11 (vote) = 300 floor 의 10×/27× miss — sample power 자체 fail (Lesson F1-2) | n=35 events = SLOOS 1990-2025 전수, AR(1) 지정 후 36-1 (CRSP cutoff). **더 늘릴 수 없음** — thin-event-study class 한계 |
| Recovery path | F2 expectation-prior layer 의무 (mechanism 변환 자체 필요) | forward 4-8 SLOOS releases (2026-Q3+) 자연 누적 — mechanism 변경 없음 |
| Outcome class | frozen-two-layer (mechanism-tradability dissociation) | **LAYER A LOCKED — event-study class** (cell-level Bonferroni + F-test + alternative event def 3 strict) |

**결론**: F1 의 frozen-two-layer 는 **mechanism-tradability dissociation** 가 본질 (학습 lock = expectation-prior layer 의무). S1 의 marginal Layer D 는 **thin-sample stat power** 가 본질 (학습 lock = thin-event-study class 정의 + OOS 부과 금지). 두 케이스를 같은 카테고리로 묶으면 portfolio rule 의 학습 lock 이 흐려짐 — 그래서 LAYER A LOCKED sub-class 분리.

---

## Five lock amendments — governance evaluation

(meta-harness governance close audit §5 평가 인용)

| Amendment | Day | Original | Amended | Governance verdict |
|---|---|---|---|---|
| §1.1 SLOOS shock def | Day 2 | level z>1.5σ first-quarter | AR(1) residual `\|z_innov\|>1.0σ` | **GOVERNANCE-OK** — BKP 2026.02 정렬, ad-hoc 아님 |
| §7 SVB cohort floor | Day 2 | ≥8 events | ≥1 (regime case study) | **GOVERNANCE-OK** — 사실에 의한 inevitable amendment |
| §1.6 IVOL proxy | Day 8-9 | "Std of CARs in most recent prior shock event" | Realized std of `Mkt-RF` 60d preceding | **GOVERNANCE-OK** — Ang et al. 2006 표준, signal leak 차단 mechanical 정당성 |
| §1.6 CCM link | Day 14 | (implicit) `ccmxpf_lnkhist` | CUSIP8 static → time-varying via dsenames.ncusip | **GOVERNANCE-OK** — WRDS USAGE block 외부 vendor 한계, workaround 자체가 contribution (4 sister repo lift) |
| §1 framework | Phase 4 | Tradable factor (Δ Sharpe ≥ 0.40 binding) | Event-study regime detection (cell-level Bonferroni binding; Sharpe supplementary) | **GOVERNANCE-OK with Gate N retroactive legitimization** — Lucca-Moench / Savor-Wilson / BKP / Bassett / Ferreira 5 prior literature 가 같은 class 의 PRIMARY 가 cell-level event-study 임을 입증, 원 lock 자체가 method-task mismatch 였음 |

5 amendments 모두 governance audit 양식 통과. Phase 4 framework reframing 은 사용자 4-round 추궁 후 의심 해소 (governance close §3).

---

## Forward sector-pattern monitor (gate 아님 — health monitoring)

`src/sloos_sector_cross_section/forward_monitor.py` (이미 scaffold) + 분기별 cron schedule.

**Trigger**: 새 SLOOS release (FRED `DRTSCILM` quarterly update, ~분기 첫 달 7~14일 발표) 후 24h 내 자동 실행.

**Per-release metrics** (3종 추적):

- (M-1) Sector pattern Spearman correlation (forward vs in-sample at 6m). ≥ 0.5 aligned / < 0.5 boundary / < 0 reversal
- (M-2) Top-6 sector sign agreement (Cons Disc / Energy / Industrials / Materials / Healthcare / Utilities). ≥ 4/6 aligned
- (M-3) F-test heterogeneity at incremental sample. p-value 단방향 추적

**LAYER A LOCKED 지위는 forward 결과와 무관** — 단순 health monitoring. forward Spearman drop 시 paper limitation 에 반영하되 demote 안 함. **단** 3 metric 모두 fail + Spearman < 0 (full reversal) 시에만 별도 governance audit trigger.

매 release 후 audit 추가: `audits/YYYY-MM-DD-S1-forward-monitor-{N}-th.md`. broadcast: portfolio-coordination Telegram mailbox (사용자 telegram-setup 활성 시).

---

## 외부 deliverable 산출 path

- **paper extraction target**: `D:/vscode/meta-harness/reports/papers/2026-05-05-sloos-sector-cross-section-paper.md` (X / β / F6 / disclosure-decay-meta-tool 와 같은 1차 PR 노출 카테고리). reports/postmortems/ 적용 부적격 (LAYER A LOCKED 지위 때문).
- **publication target advisory** (S1 sub-agent 또는 사용자 결정):
  - T1 (즉시, 2-3주 내): SSRN preprint
  - T2 (cross-list): arXiv q-fin
  - T3 (Federal Reserve): FEDS Note (BKP 저자와 직접 dialogue 가능, 2026.02 follow-up positioning)
  - T4 (advisor co-author): J Mon Econ / RFS / J Finance — 별도 협의
- **GitHub public push**: 사용자 명시 승인 후 (X / F6 답습), target `github.com/Crane-lupert/sloos_sector_cross_section`
- **shared_utils 추출 4 모듈** (P3 follow-up audit): time-varying CCM link / AR(1) macro shock / F-test heterogeneity / DRTSCIS robustness pattern → portfolio-coordination/shared_utils/ 외부 deploy + 4 sister repo lift (factor_zoo / sec_comment / 8-K / climate)

---

## Audit pointers

- **governance close**: `D:/vscode/meta-harness/audits/2026-05-05-S1-governance-close-layer-a-locked-event-study.md` (close 결정 + Gate N 신설 + 5 amendment 평가 + F1 vs S1 differentiation)
- **close propagation**: `D:/vscode/meta-harness/audits/2026-05-05-S1-close-propagation.md` (P1/P2/P3 verification PASS)
- **comprehensive research report**: `D:/vscode/meta-harness/audits/2026-05-05-sloos_sector_cross_section-comprehensive-research-report.md` (985줄 19 sections + 4 appendices)
- **S1-side daily/phase audits** (17 files): `audits/2026-05-05-S1-*.md` — bootstrap, day1/2/3/5/7/9/10/11/14, phase0/3/3v2/4-framing/4-eod, sign-conditional, healthcare-outlier, courier-followup
- **comprehensive Phase 4 framing audit**: `audits/2026-05-05-S1-phase4-framing.md` + `2026-05-05-S1-phase4-eod.md`

---

## Reproducibility

```bash
git clone <repo>  # github.com/Crane-lupert/sloos_sector_cross_section (사용자 승인 후 public)
cd sloos_sector_cross_section
cp .env.example .env  # FRED_API_KEY required (free)
uv sync --extra dev
uv run pytest         # 105 tests, all green

# Forward monitor (run after each new SLOOS release)
uv run python -m sloos_sector_cross_section.forward_monitor
```

WRDS courier (read-only) 의존 — `crsp_a_stock.dsf` + `crsp_a_stock.dsenames` + `comp_na_daily_all.{names,company}`. Real `ccmxpf_lnkhist` USAGE-blocked 시 dsenames-time-varying 워크어라운드 자동 사용. CUSIP8 join 95.5% R3000 universe coverage.

---

## QR Scout portfolio context

- **5번째 1차 PR piece** (X / β / F6 / disclosure-decay-meta-tool 다음)
- **LAYER A LOCKED 두 번째** + **first event-study sub-class**
- **Macro/Credit pod first LOCKED** (V1 frozen-two-layer / S1 LOCKED 으로 sub-pod 분리 확인)
- **method maturity flagship** — 5 lock amendment 투명 audit + Phase 4 reframing 정당성 + 3 panel version bias trail
- **infrastructure asset 4 sister repo lift** (time-varying CCM link 워크어라운드 — `factor_zoo_decay_audit` / `sec_comment_letter_alpha` / `eight_k_non_reliance_llm` / `climate_transition_llm`)

---

## Bayesian prior post-S1 (n=13)

- LAYER A LOCKED (combined): 2/13 = 15.4% (F6 + S1)
  - tradable-factor sub-class: 1/13 = 7.7% (F6)
  - event-study sub-class: 1/13 = 7.7% (S1) ← first instance
- frozen-two-layer (combined): 7/13 = 53.8%
- TERMINAL: 1/13 (X3); Killed input: 1/13 (Y); Closed Option 4: 1/13 (Z); frozen-pending-vendor: 1/13 (D-q2.2)

신규 prior: thin-event-study class 후보 시 LAYER A LOCKED — event-study class odds ~25-35% (S1 + F6 escape mechanism partial fit), frozen-two-layer (event-study sub-mode) ~40-50%, ABANDONED (cell-level fail) ~15-25%.

---

**Status code marker. STOP per CLAUDE.md §5 — gh push 사용자 명시 승인 후만**.
