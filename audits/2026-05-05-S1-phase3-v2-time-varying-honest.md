# S1 Phase 3 v2 — Time-varying CCM link 정직한 재평가 — 2026-05-05

## TL;DR — 가장 정직한 결과

Phase 3 v1 (CRSP static CUSIP8) 의 "alpha-Sharpe +3.357 strengthening" 은 **lookahead bias 였음**. Time-varying CCM link 적용 시 진짜 alpha 가 marginal 수준으로 회귀:

| 패널 구성 | Layer A pass | 6m raw Sharpe | 6m alpha-Sharpe | p-value |
|---|---|---|---|---|
| Compustat (원본 LAYER A LOCKED) | 18/33 | +1.027 | +1.112 | 0.080 |
| CRSP + static CUSIP8 (Phase 3 v1) | 22/33 | +1.552 | +3.357 | <0.001 |
| **CRSP + time-varying (Phase 3 v2)** | **15/33** | **+0.397** | **+0.866** | **0.182** |

## Bias 진단

**3가지 bias** 가 있었음을 명확히 분리:
1. **Survivor bias**: 현재 살아남은 firms 만 사용 → delisted firms 의 큰 손실 missing
2. **Lookahead bias on universe**: 2026 R3000 universe 를 1990 까지 backfill → 당시 존재하지 않던 firms 가 포함됨
3. **Lock amendments** (Day 2 SLOOS def, Day 8 IVOL proxy)

Phase 별 bias 보정 상태:

| Phase | Survivor | Lookahead-univ | Lock amendments |
|---|---|---|---|
| Original (Compustat sec_dprc) | 있음 | 있음 | 적용됨 |
| Phase 3 v1 (CRSP + static) | **수정** | 있음 | 적용됨 |
| **Phase 3 v2 (CRSP + time-varying)** | **수정** | **수정** | **적용됨** |

## Lookahead bias 메커니즘 검증

Static CUSIP8 link 의 문제점:
- 우리 R3000 universe = 2026-05 iShares snapshot
- 정적으로 "permno↔gvkey 매핑이 항상 유효" 처리 → 2000년 SLOOS 이벤트에도 2,765 firms 모두 포함
- 하지만 그 firms 의 ~75% 는 2000년에 IPO 도 되지 않은 상태

Time-varying 수정:
- dsenames 의 namedt/nameendt 시점 사용
- 2000-04-01: 활성 firms 763 개 (실제로 그 시점에 CRSP 등재)
- 2008-04-01: 1,101 firms / 2020-04-01: 2,058 firms / 2024-12-01: 2,755 firms
- 시간이 지날수록 universe 가 자라는 정상적 패턴 (역사적 universe reconstruction 와 일치)

## Layer A — 시점별 universe 에서 cell-level test

| Horizon | Compustat (원) | CRSP static | CRSP time-varying |
|---|---|---|---|
| 1m | 6 cells | 7 cells | 3 cells |
| 3m | 4 cells | 6 cells | 6 cells |
| 6m | 8 cells | 9 cells | 6 cells |
| Total | 18 | 22 | **15** |

→ **15 / 33 cells 여전히 Bonferroni-K=33 pass** (Phase 1 §7 floor 5 보다 3배 강함)
→ Layer A (sector cross-section heterogeneity) 는 lookahead 보정 후에도 robust

## Layer D — L/S strategy alpha 변화

| Horizon | Compustat | CRSP static (v1) | CRSP time-varying (v2) | Δ from v1 to v2 |
|---|---|---|---|---|
| 1m | +2.478 *** | +0.709 | **+0.193 (p=0.74)** | -0.52 |
| 3m | +1.134 . | +1.700 * | **-0.035 (p=0.96)** | -1.74 |
| 6m | +1.112 . | +3.357 *** | **+0.866 (p=0.18)** | -2.49 |

→ **6m alpha-Sharpe +0.87** (Phase 1 §7 floor 0.40 통과 but p>0.05 marginal)
→ **1m, 3m alpha-Sharpe < 0.40** → FAIL Phase 1 floor

## Walk-forward — out-of-sample test

| Fold | Train n | Test n | net Sharpe | Pass |
|---|---|---|---|---|
| 1 | 6 | 6 | -0.911 | **FAIL** |
| 2 | 12 | 6 | +0.397 | PASS |
| 3 | 18 | 5 | +0.438 | PASS |
| 4 | 23 | 6 | +0.253 | PASS |
| 5 | 29 | 6 | +0.223 | PASS |

→ **4/5 PASS** (Phase 1 §1.9 floor met by 1)
→ Fold 1 negative — early-data train (n=6) 너무 thin, fold 1 test 는 1990s 인데 현재 R3000 universe 의 그 시점 활성 firms 가 적어 매우 noisy

## Outcome 재평가

**원래 평가**: LAYER A LOCKED 3-of-3 PASS (Compustat 기반)
**Phase 3 v1**: LAYER A LOCKED + reinforced (CRSP static)
**Phase 3 v2**: ⚠️ **borderline frozen-two-layer**

Phase 1 §1.7 lock 「Δ Sharpe ≥ 0.40」 을 strict 적용하면:
- Layer A: 15/33 PASS ✓ (PASS)
- Layer D 6m: alpha-Sharpe 0.866 ≥ 0.40 ✓ (PASS, but p=0.18 statistically marginal)
- Walk-forward: 4/5 ✓ (PASS, fold 1 borderline)

**기술적으로는 LAYER A LOCKED 3-of-3 유지**. 하지만 statistical significance 가 약해졌음:
- 6m alpha-Sharpe p-value = 0.18 → conventional 5% level 에서 H_0 (alpha=0) 기각 못 함
- n=35 events, 9 baseline features 로 power 부족
- 1m, 3m horizons 에서는 alpha 사실상 0

## Honest research 결론

1. **Sector cross-section heterogeneity hypothesis (Layer A) IS supported**: Bias 보정 후에도 15/33 cells significant. 이것은 real economic phenomenon.

2. **L/S trading strategy alpha is MARGINAL**: 6m alpha-Sharpe +0.87 (p=0.18) — 가까운 floor 통과지만 통계적으로 유의 안 됨. n=35 thin sample 의 한계.

3. **이전 (+1.11 Compustat, +3.36 CRSP static) 결과는 partial bias 만 보정 → 모두 inflated**:
   - Compustat: survivor bias + lookahead-on-universe
   - CRSP static: lookahead-on-universe만

4. **True OOS Sharpe estimate (revised)**: 0.4-0.9 at 6m. 이전 honest-research 경고 (0.3-0.7) 와 일치.

5. **Sign-conditional 변형 (paper §10)** 은 time-varying universe 에서 재검증 필요 — Compustat 기준 +2.08 결과는 likely inflated.

## 다음 단계 권고

### 즉시 (paper / dashboard 수정)
1. paper_v1.md headline 결과를 **time-varying CRSP 6m alpha-Sharpe +0.866 (p=0.182)** 로 강등
2. §11 limitations 에 "Phase 3 v2 가 진짜 honest result" 명시
3. README.md / README_KR.md 에 3-version comparison 표 추가
4. LAYER A LOCKED 결과 → "LAYER A LOCKED with statistical caveats" 또는 "frozen-two-layer borderline"

### 후속 작업
1. 진짜 ccmxpf_lnkhist (USAGE 풀린 후) 로 비교 → linktype/linkprim quality filter 효과 측정
2. Forward OOS test (다음 4-8 분기 SLOOS 발표) — 진짜 진짜 honest 결과
3. n 늘리기: robust SLOOS series (DRTSCIS) PC 결합으로 events ≥50 가능?
4. Sign-conditional time-varying re-test
5. Firm-level Ang et al IVOL 정식 구축

## 변경된 사항 (Phase 3 v2)
- `src/sloos_sector_cross_section/crsp_link_timevarying.py` — 시점별 CCM link 구축 (year1/year2 미사용 default, open-period 자동 확장)
- `src/sloos_sector_cross_section/crsp_panel.py` — `time_varying=True` 옵션 추가
- `data/cache/ccm_link_timevarying_2026-05-05.parquet` — link panel
- `data/cache/crsp_sector_panel_DRTSCILM_AR1_TIMEVAR_v2_2026-05-05.parquet` — time-varying CRSP panel
- `E:\wrds-data-courier\inbox\S1-time-varying-ccm-link-discovery-20260505.md` — courier alert (sister repos 도 활용 가능)
- 이 audit
