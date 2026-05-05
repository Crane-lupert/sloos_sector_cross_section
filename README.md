# sloos_sector_cross_section (S1)

**Project class**: QR Scout discovery / alpha-research (Macro/Credit pod first)

## Hypothesis

Fed Senior Loan Officer Opinion Survey (SLOOS) C&I lending standard tightening shock event (분기별 발표, z-score > 1.5σ rolling 40-quarter) → forward {1mo, 3mo, 6mo} 11 GICS sector cross-section CAR cyclical heterogeneity:
- Cyclical (Industrials / Consumer Disc / Financials / Energy / Materials) negative response
- Defensive (Staples / Healthcare / Utilities / Comm Services / Real Estate) muted response
- Post-2023.Q3 SVB shock cohort sub-sample = narrow novel angle

## Goal

Layer A (Welch t Bonferroni-K=33 critical t≈3.04, ≥5 cells PASS) + Layer D (incremental Sharpe Δ ≥ 0.4 vs FF5+Mom+IVOL+SRF+E-CSI 5-component baseline) + Walk-forward (5-fold chronological ≥4/5 fold positive net-cost) → **LAYER A LOCKED** 2nd-of-N portfolio entry.

## Outcome class

- **LAYER A LOCKED**: 3-of-3 PASS → paper + Streamlit + bilingual README + GitHub public push
- **frozen-two-layer**: 2-of-3 PASS → 6th frozen-two-layer instance, post-mortem-negative-result-template
- **ABANDONED**: 1-of-3 → ABANDONED.md
- **Fed scoop trigger**: weekly monitor → 14d 안 freeze 가능

## Data sources

- **SLOOS**: FRED `DRTSCILM` (primary, 1990.Q1-2026.Q1, 140+ quarters) + 5 robust series
- **Equity cross-section**: WRDS courier `comp_na_daily_all.secd` × `comp.security` × `comp.company.gsector`
- **R3000 universe**: iShares IWB/IWN/IWM holdings public CSV
- **FF5 + Mom**: Ken French data library public CSV
- **IVOL / SRF / E-CSI**: 자체 계산

## Phases

- Phase 0 (Day 1-3): SLOOS fetch + universe + shock construct + sector panel + n_min audit
- Phase 1 (Day 4-9): Layer A Bonferroni-33 + 5-component baseline build + Layer D Δ Sharpe + Gate M
- Phase 2 (Day 10-12): Gate L lookahead + Gate K subperiod + Walk-forward 5-fold + SVB cohort sub-finding
- Day 13-14: outcome decision + paper + dashboard + bilingual README + GitHub push (LAYER A LOCKED 시)

## 강제 규칙

CLAUDE.md §1 17종 (QR Scout discovery flavor — narrow novel + 5-component baseline + Phase 0 #8 weekly Fed scoop monitor 등).

## 참고 audits

- `D:/vscode/meta-harness/audits/2026-05-05-S1-sloos-reference-validation.md` (~700 lines, prior art deep dive + Phase 0/1/2 plan + Lock 28+개)
- `D:/vscode/meta-harness/audits/2026-05-05-S1-overnight-start-prompt.md` (V4 paste-ready)
- `D:/vscode/meta-harness/audits/2026-05-05-S1-CLAUDE.md.draft.md`
- `D:/vscode/meta-harness/audits/2026-05-05-S1-settings.json.template.md`

## Setup

```bash
uv sync
# .env file 작성 (gitignored): FRED_API_KEY / OPENROUTER_API_KEY / GITHUB_TOKEN / PROJECT_NAME
uv run pytest
```

## Status

**LAYER A LOCKED 3-of-3 PASS** (2026-05-05).

| Gate | Lock spec | Measurement | Status |
|---|---|---|---|
| Layer A (Welch t-test + Bonferroni K=33) | ≥ 5 cells significant | **18 / 33** | PASS (3.6× floor) |
| Layer D (5-component baseline absorption) | Δ Sharpe ≥ 0.40 | **+1.112** at 6m | PASS (2.8× floor) |
| Walk-forward (5-fold ≥ 4/5 positive net-cost) | ≥ 4/5 | **5/5** | PASS (100%) |
| Gate K subperiod | ≥ 0.5 | 0.95 | PASS |
| Gate L lookahead (honest shift) | ≥ 0.5 | 0.79 | PASS |
| Gate M net-of-cost | ≥ 0 | +1.02 | PASS |
| Walk-forward fold range | — | +0.41 to +2.77 net Sharpe | all 5 positive |

### Phase 3 honest revision (2026-05-05): CRSP survivor-bias correction
| Variant | Raw Sharpe | Alpha-Sharpe (5-comp absorbed) | p-value |
|---|---|---|---|
| Compustat unsigned 6m | +1.027 | +1.112 | 0.080 |
| **CRSP unsigned 6m (survivor-bias-corrected)** | **+1.552** | **+3.357** | **<0.001** |
| CRSP sign-conditional 6m | +1.590 | +3.244 | <0.001 |

Counterintuitive finding: survivor bias correction **strengthens** the headline. Compustat under-counts the SHORT basket (Healthcare/IT) because delisted firms' losses are absent. CRSP captures them → L/S 6m alpha-Sharpe triples.

1m horizon DOES show survivor-bias inflation: alpha-Sharpe drops +2.48 → +0.71 (p=0.22 marginal). Original 1m result was overstated.

CCM link via CUSIP8 (95.4% R3000 coverage) — real `ccmxpf_lnkhist` USAGE-blocked in WRDS subscription. Time-varying linkage is a known limitation. See `audits/2026-05-05-S1-phase3-honest-revision.md`.

Lock amendments (audit trail):
- Phase 0 §1.1 SLOOS shock: amended Day 2 to AR(1) residual `|z_innov|>1.0σ` (was `level z>1.5σ rolling 40q first-quarter`). Reason: original gave 5 events << 30 floor due to AR(1) ρ=0.86 high persistence.
- §7 SVB cohort floor: amended Day 2 to ≥1 (regime case study, not co-equal sample). Reason: only ~11 SVB releases exist.
- IVOL proxy: revised Day 8-9 from "prior-event cross-section std" (degenerate, signal leak) to "realized std of Mkt-RF over 60td prior" (Ang et al 2006 standard).

Artifacts:
- `analysis/paper_v1.md` — full English reproducibility paper
- `analysis/README_KR.md` — Korean distill
- `dashboard/app.py` — Streamlit MVP
- `audits/2026-05-05-S1-*.md` — 8 daily audit files documenting locks + amendments
- `data/cache/*.parquet` — pipeline outputs (gitignored, regenerated by `uv run pytest` + per-module scripts)

Test count: 94/94 passing.

GitHub public push pending user approval (high-blast-radius). Repository scaffold and all artifacts complete.
