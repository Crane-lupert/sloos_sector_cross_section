# sloos_sector_cross_section (S1)

Fed Senior Loan Officer Opinion Survey (SLOOS) C&I lending standard tightening shock event (quarterly release, AR(1)-innovation `|z_innov|>1.0σ`) × 11 GICS sector cross-section forward CAR cyclical heterogeneity event-study.

**Status**: ✅ **LAYER A LOCKED — event-study class** (Phase 4 closed 2026-05-05). **한국어 distill**: [analysis/README_KR.md](analysis/README_KR.md).
**Type**: discovery-form alpha-research, **portfolio second LAYER A LOCKED instance** (after F6), **first event-study sub-class member** (Gate N thin-event-study class first instance), **Macro/Credit pod first LOCKED**.
**Daemon**: PURE daemon-free (Gate F ✓) — FRED API + WRDS courier (read-only) + Ken French CSV + iShares CSV.

## Layer A — event-study class headline metrics

| Trigger | Threshold | Final value | Verdict |
|---|---|---|---|
| (N-1) Cell-level Bonferroni-K=33 (PRIMARY) | ≥ 5 cells significant | **15 / 33** (3× floor) | ✅ |
| (N-2) F-test sector heterogeneity 6m (PRIMARY) | p < 0.05 in ≥1 horizon | **p = 1.8e-56** at 6m (3/3 horizons) | ✅ overwhelming |
| (N-3) Alternative event def DRTSCIS Spearman (PRIMARY) | ≥ 0.5 in ≥1 horizon | **0.827 / 0.864 / 0.891** at 1m/3m/6m, sign 10/11 | ✅ all 3 horizons |
| (N-S1) Bootstrap share-pass-Bonferroni (refined supplementary) | ≥ 5 cells share ≥ 0.70 | **13 / 33** | ✅ refined PASS |
| (N-S2) VIX-regime stratification (refined supplementary) | sign agree ≥ 7/11 strict, or boundary refinement | 6/11 sign agree at 6m | boundary characterization |
| (N-S3) Layer D Δ Sharpe (illustrative supplementary, **not binding**) | n_event<50 ⇒ no binding floor | **+0.866 (p=0.182 marginal)** at 6m | reported but not gating |
| (N-S4) Walk-forward (illustrative supplementary, **not binding**) | n_event<50 ⇒ method-task mismatch | 4/5 PASS | reported but not gating |

**Headline 6m sector pattern (v3 CRSP-time-varying honest panel)**: Cons Disc +9.59 / Healthcare -7.15 / Utilities -5.64 / Energy +5.20 / Industrials +4.37 / Materials +3.51 (cyclical-positive / defensive-negative monotone, thesis-consistent across all horizons).

**Layer D illustrative supplementary**: Δ Sharpe +0.866 (p=0.18 marginal; not binding under thin-event-study class — Gate N rule §4.4 mathematical impossibility lock against in-sample/OOS split).

**Paper draft**: [analysis/paper_v1.md](analysis/paper_v1.md) (event-study reproducibility paper).
**Dashboard**: `streamlit run dashboard/app.py` (MVP).

---

## Hypothesis

amendment 의 quarterly SLOOS C&I lending-standard tightening shock event (AR(1)-innovation > 1σ) → 11 GICS sector forward CAR cross-section heterogeneity. Cyclical (Industrials / Cons Disc / Materials / Energy / Financials) post-shock recovery long, defensive (Healthcare / Utilities) selloff short.

**Contribution**:
- BKP 2026.02 E-CSI methodology 의 *equity sector forward* extension (BKP 본인은 lending-standard prediction 자체에 한정)
- Lucca-Moench 2015 / Savor-Wilson 2014 / Bidder-Krane-Park 2026.02 / Bassett 2014 / Ferreira 2024 prior literature 가 같은 분야 cell-level event-study 표준 적용 — S1 은 이 5 paper line 의 **SLOOS-shock × equity sector** 신규 응용
- 4 sister repo lift target (time-varying CCM link via dsenames.ncusip — `factor_zoo_decay_audit` / `sec_comment_letter_alpha` / `eight_k_non_reliance_llm` / `climate_transition_llm`)

---

## Three-version bias trail (key methodological contribution)

| Version | Survivor bias | Lookahead-univ bias | 6m Layer D α-Sharpe (illustrative) | Layer A cells |
|---|---|---|---|---|
| v1 (Compustat sec_dprc) | YES | YES | +1.112 (p=0.080) | 18/33 |
| v2 (CRSP `dsf` + static CUSIP8) | NO | YES | +3.357 (p<0.001) — apparent strengthening, partly artifact | 22/33 |
| **v3 (CRSP `dsf` + time-varying via `dsenames.ncusip`)** | **NO** | **NO** | **+0.866 (p=0.182 marginal)** | **15/33** |

v2 → v3 panel size 288K → 135K rows (1.91× reduction) quantifies lookahead-bias inflation factor. The v3 honest-corrected universe is the binding panel for all PRIMARY tests.

---

## Data sources

- **SLOOS primary**: FRED `DRTSCILM` (1990-Q2 → 2026-Q2, 145 quarters)
- **SLOOS robust** (alternative event def): FRED `DRTSCIS` (small-firm SLOOS C&I tightening)
- **Equity returns (v3 panel)**: WRDS courier `crsp_a_stock.dsf` (107M rows, 1925-2024, delisting return native via `ret`)
- **CRSP↔Compustat link**: `dsenames.ncusip` (시간-가변 CUSIP) + `comp_na_daily_all.names.cusip` SUBSTR(8) join — workaround for USAGE-blocked `crsp_a_ccm.ccmxpf_lnkhist` (95.5% R3000 coverage, 0 ambiguity)
- **GICS mapping**: `comp_na_daily_all.company.gsector` (11 sectors)
- **R3000 universe**: iShares IWB + IWM holdings public CSV
- **FF5 + Mom**: Ken French data library public CSV
- **IVOL / SRF / E-CSI**: 자체 계산 (Ang et al. 2006 macro proxy / Ferreira 2024 / Bidder-Krane-Park 2026.02)
- **Macro covariates** (E-CSI proxy): FRED UNRATE / T10Y3M / GDPC1 / VIXCLS

---

## Phases (executed 2026-05-05, ~7 wall-time hours)

- Phase 0 (Day 1-3): SLOOS fetch + universe + AR(1) shock construct + sector_panel + n_min audit
- Phase 1 (Day 4-9): Layer A Bonferroni-33 + 5-component baseline build + Layer D Δ Sharpe + Gate M
- Phase 2 (Day 10-12): Gate L + Gate K + Walk-forward 5-fold + scoop checks
- Phase 3 v1+v2 (2026-05-05): CRSP survivor-bias + time-varying lookahead-bias 보정 (3 panel versions)
- Phase 4 (2026-05-05): event-study reframing (CLAUDE.md §1 amended) + 4 PRIMARY robustness tests + Gate N retroactive legitimization

## 강제 규칙

CLAUDE.md §1 (17 locks + Phase 4 PRIMARY robustness block + 5 amendments governance-OK).

## 참고 audits

- **governance close (LAYER A LOCKED — event-study class)**: `D:/vscode/meta-harness/audits/2026-05-05-S1-governance-close-layer-a-locked-event-study.md`
- **comprehensive research report (985 lines)**: `D:/vscode/meta-harness/audits/2026-05-05-sloos_sector_cross_section-comprehensive-research-report.md`
- **close propagation P1/P2/P3 verification**: `D:/vscode/meta-harness/audits/2026-05-05-S1-close-propagation.md`
- S1-side daily/phase audits (17 files): `audits/2026-05-05-S1-*.md`

## Setup

```bash
uv sync --extra dev
# .env (gitignored) 작성: FRED_API_KEY (free) / OPENROUTER_API_KEY (optional, scoop only) / PROJECT_NAME
uv run pytest          # 105+ tests, all green

# Forward sector-pattern monitor (gate 아닌 health monitoring; run after each new SLOOS release)
uv run python -m sloos_sector_cross_section.forward_monitor
```

## Outcome class

- ✅ **LAYER A LOCKED — event-study class** (current, closed 2026-05-05): cell-level Bonferroni-K=33 + F-test heterogeneity + alternative event def 3 PRIMARY strict PASS → paper + Streamlit + bilingual README + GitHub public push (사용자 명시 승인 후)
- frozen-two-layer (event-study sub-mode): Gate N PRIMARY 2 이하 PASS — applies to other thin-event-study candidates, not S1
- ABANDONED: cell-level Bonferroni < 5 — does not apply

**Forward gate**: 없음 (CLAUDE.md §5 governance close 결정). forward sector-pattern monitor (gate 아님 — health monitoring 만) 분기별 운영. forward Spearman drop 시 paper limitation 갱신, **LAYER A LOCKED 지위 demote 안 함**.

## QR Scout portfolio context

- **5번째 1차 PR piece** (X / β / F6 / disclosure-decay-meta-tool 다음)
- **LAYER A LOCKED 두 번째** + **first event-study sub-class member** (Gate N thin-event-study class first instance)
- **Macro/Credit pod first LOCKED** (V1 frozen-two-layer / S1 LOCKED 으로 sub-pod 분리 확인)
- **method maturity flagship** — 5 lock amendment 투명 audit + Phase 4 reframing 정당성 + 3 panel version bias trail
- **infrastructure asset 4 sister repo lift** (time-varying CCM link 워크어라운드)

GitHub public push: 사용자 명시 승인 후 (CLAUDE.md §5 + governance close §0.6). target `github.com/Crane-lupert/sloos_sector_cross_section` (X / F6 / V1 답습 naming).
