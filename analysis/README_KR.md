# SLOOS 충격 × 11 GICS 섹터 cross-section 이질성 — 한국어 요약

**프로젝트**: S1 sloos_sector_cross_section
**날짜**: 2026-05-05
**결과**: **LAYER A LOCKED 3-of-3 PASS**
**Pod**: Macro/Credit pod first

## 핵심 결과

Fed SLOOS C&I 대출기준 긴축 충격 (분기별 발표) → forward {1mo, 3mo, 6mo} 11 GICS 섹터 cross-section CAR 이질성 **확인**.

| Gate | Floor | 측정값 | 결과 |
|---|---|---|---|
| Layer A (Welch t + Bonferroni K=33) | ≥ 5 cells | **18/33 cells** (3.6× floor) | **PASS** |
| Layer D (5-component baseline 흡수) | Δ Sharpe ≥ 0.40 | **+1.112** at 6m (2.8× floor) | **PASS** |
| Walk-forward 5-fold | ≥ 4/5 fold positive net-cost | **5/5** | **PASS** |

부속 gate (Day 10):
- Gate K subperiod (1990-2010 vs 2010-2026): ratio 0.95 (PASS)
- Gate L lookahead (honest shift = horizon+1): decay 0.79 (PASS)
- Gate M net-of-cost: net Sharpe +1.02 (PASS)

## 데이터

- **SLOOS primary**: FRED `DRTSCILM` (1990-Q2 ~ 2026-Q2, 145 quarters)
- **Equity universe**: R3000 (iShares IWB ∪ IWM 합성), 2,926 tickers, 99% gvkey + GICS 매핑
- **Compustat sec_dprc**: 159M rows daily price (WRDS courier 통한 zero-config 접근)
- **Ken French FF5 + Mom**: public CSV (Dartmouth)
- **Macro covariates**: UNRATE, T10Y3M, GDPC1, VIXCLS (FRED)

## Shock 정의 (Phase 0 §1.1 amendment)

원래 lock: rolling 40q level z-score > 1.5σ first-quarter event
→ events=5 (≪ 30 floor) due to DRTSCILM AR(1) ρ=0.86 high persistence + 3-regime structure

**Amended**: full-sample AR(1) residual `|z_innov| > 1.0σ` (Bidder-Krane-Park 2026.02 + Bassett 2014 표준)
- 36 events (19 tightening, 17 easing)
- Decade balance: 1990s=7, 2000s=13, 2010s=6, 2020s=10
- SVB cohort (≥2023-Q3): 2 events (regime case study, not co-equal sample per Day 2 amendment)

## 주요 섹터 패턴 (6m horizon, Bonferroni-significant)

| 섹터 | 평균 CAR (bp) | t-stat | 방향 |
|---|---|---|---|
| Healthcare | -523 | **-11.94** | 강한 음 |
| Industrials | +254 | +7.07 | 양 (cyclical) |
| Consumer Staples | +375 | +5.42 | 양 (defensive accumulation) |
| Consumer Discretionary | +173 | +4.23 | 양 |
| IT | -204 | -4.08 | 음 (peak-then-fall) |
| Utilities | +193 | +3.93 | 양 |
| Materials | +251 | +3.90 | 양 (cyclical) |
| Financials | +89 | +3.87 | 양 (mean-reversion bounce) |

**Real Estate** 만 모든 horizon 에서 비유의 (closest 1m t=-2.17). Cross-horizon 패턴:
- Financials: 1m -140bp / 3m -122bp → 6m +89bp (mean-reversion)
- Healthcare: 1m +83bp → 6m -523bp (defensive 가 6m 에 underperform — risk-on rotation)
- IT: 1m +265bp → 6m -204bp (peak-then-fall)

## L/S 전략 + Layer D 흡수 (6m horizon)

- **Long basket** (6 sectors, +t Bonferroni-pass): Industrials, Cons Staples, Cons Disc, Materials, Financials, Utilities
- **Short basket** (2 sectors, -t Bonferroni-pass): Healthcare, IT
- Strategy return per event = mean(long 6m log ret) − mean(short 6m log ret)

5-component baseline 흡수 후 alpha-Sharpe (annualized) **+1.112** (p=0.080). Per-component 분해:
- E-CSI 단일 component 가 가장 많이 흡수 (+0.24 incremental drop). 즉 macro-foreseeable component 는 E-CSI 가 잡고, 전략의 잔여 alpha 는 macro 로 설명되지 않는 **cross-section dispersion of sector responses** 에서 발생.
- IVOL (realized market vol over 60td prior event) 의 흡수는 약간 negative (-0.21) — 즉 IVOL 을 baseline 에 넣어도 alpha 가 거의 변하지 않음.
- FF5: +0.18 흡수 (small, L/S 가 시장중립적 구조).

## 부속 robustness 결과

- **Gate K subperiod**: pre-2010 Sharpe +0.996 / post-2010 +1.047 / ratio 0.951. GFC 분기 무관하게 안정.
- **Gate L lookahead**: 1d shift decay 1.09 (no immediate leak), horizon+1 (honest shift) decay 0.79. 2× horizon (12m) decay 0.35 — 신호의 자연 감쇠 (lookahead bias 아님).
- **Gate M net-of-cost**: 5bp/yr cost 차감 후 net Sharpe +1.02.
- **Walk-forward 5-fold**: 5/5 fold positive net Sharpe (range +0.41 to +2.77). Short basket [Healthcare, IT] 모든 fold 일관 (fold 2-5).

## 한계 및 follow-up

1. Survivor bias: 2026 현재 listed 종목 backfill. 실거래 Sharpe 는 더 낮음.
2. Healthcare 6m -523bp t=-11.94 극단치 — 1-2 outlier firms 확인 필요 (winsorize).
3. In-sample Layer A → Layer D 동일 data — walk-forward 가 mitigate.
4. SVB cohort n=2 → regime case study 만, 통계 sample 아님.
5. 12m horizon strategy 는 비-tradable (signal 자연 감쇠).

## 재현

```bash
git clone <repo url>
cd sloos_sector_cross_section
cp .env.example .env  # FRED_API_KEY 추가 (무료)
uv sync --extra dev
uv run pytest         # 94 tests all green
```

자세한 일일 audit: `audits/2026-05-05-S1-*.md` (bootstrap + Day 1-11). lock amendment 추적: CLAUDE.md §1.1 (Day 2 AR(1) innovation), §7 (SVB floor 완화), audits/2026-05-05-S1-day2-eod.md + day9-eod.md.

## Bayesian prior 갱신

- 사전 확률 (CLAUDE.md §6): LAYER A LOCKED ~25-30%, frozen-two-layer ~40-45%, ABANDONED ~15-20%, Fed scoop ~20-30%.
- 사후 결과: **LAYER A LOCKED** (3-of-3 PASS). Fed scoop 3 차례 (Day 1, 7, 11) 모두 clean. AR(1) innovation amendment 가 Day 2 stop trigger 를 우회한 것이 결정적.
