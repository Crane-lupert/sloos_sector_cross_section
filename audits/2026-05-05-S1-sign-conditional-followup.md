# S1 follow-up: Sign-conditional L/S strategy + walk-forward — 2026-05-05

## Trigger
Paper §10 introduces a sign-conditional L/S variant exploiting the §9 sign-asymmetry. This follow-up verifies the variant is also walk-forward robust.

## Sign-conditional strategy at 6m horizon (full sample)
Per-event basket selection by shock sign:

| Sign | Long basket | Short basket |
|---|---|---|
| TIGHTEN (n=19 events) | [Materials, Industrials, Cons Disc, Cons Staples, Utilities] | [Healthcare] |
| EASE (n=17 events) | [Energy, Industrials, Cons Staples, Financials] | [Healthcare] |

Healthcare is short on both signs (Bonferroni-pass negative on both sub-cells).

## Result vs baseline

| Strategy | n | Raw Sharpe ann. | Alpha-Sharpe ann. | α p-value | R² |
|---|---|---|---|---|---|
| Unsigned L/S (paper §6) | 35 | +1.027 | +1.112 | 0.080 | 0.675 |
| **Sign-conditional L/S** | **36** | **+1.250** | **+2.078** | **0.0021** | 0.643 |

→ Sign-conditional gives +22% raw Sharpe / +87% alpha-Sharpe / 38× lower p-value.

## Walk-forward 5-fold verification

For each fold: refit Layer A signed on train events, derive sign-specific baskets, apply per shock-sign on test.

| Fold | Train n | Test n | Test mean | Test Sharpe ann | Test net Sharpe | Pass |
|---|---|---|---|---|---|---|
| 1 | 6 | 6 | +6.53% | +1.574 | +1.569 | PASS |
| 2 | 12 | 6 | +0.07% | +0.015 | +0.004 | borderline PASS |
| 3 | 18 | 6 | +6.90% | +7.257 | +7.221 | PASS |
| 4 | 24 | 6 | +7.93% | +1.505 | +1.497 | PASS |
| 5 | 30 | 6 | +4.58% | +0.811 | +0.805 | PASS |

→ **5/5 folds PASS** (≥4/5 floor exceeded). Fold 2 is borderline (+0.004 net Sharpe) but technically positive.

## Observations
1. Fold 3 has +7.26 Sharpe — the small sample size (n=6) leads to high noise; this is one of the high-variance test sets. Fold 5 (+0.81) is a more representative test-period Sharpe.
2. The sign-conditional baskets in early folds (small training data) sometimes fall back to top-2/bot-2 by t for one of the two signs because of insufficient Bonferroni-pass cells. This fallback is principled and the resulting Sharpe remains positive.
3. The borderline fold 2 (+0.004) suggests the strategy is sensitive to specific clusters of events. Real-trading robustness check would benefit from an even longer SLOOS history if available.

## Conclusion
Sign-conditional L/S variant is operationally preferred: stronger in-sample results (alpha-Sharpe +2.08 vs +1.11) AND walk-forward robust (5/5 folds positive). Recommended as the headline strategy for follow-up paper publication.

## Tests
Existing 94 tests still all pass. No new tests added (sign-conditional is a research extension, not a locked module — testing would require freezing the methodology first).
