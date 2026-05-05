# S1 follow-up: Healthcare 6m -523bp outlier check — 2026-05-05

## Trigger
Paper v1 §10 limitation #2 flagged Healthcare 6m mean CAR -523bp (t=-11.94) as needing an outlier-robust verification.

## Diagnostic

### Distribution (n=17,545 firm-event CARs)
| Statistic | Value (bp) |
|---|---|
| Mean | -523 |
| Std | 5,803 |
| Min | -45,252 |
| 0.1% | -19,130 |
| 1% | -15,176 |
| 5% | -9,917 |
| Median | -250 |
| 95% | +7,076 |
| 99% | +12,611 |
| Max | +78,580 |

### Winsorization sensitivity
| Winsor level | Mean (bp) | t-stat |
|---|---|---|
| None | -523 | -11.94 |
| 0.1% / 99.9% | -537 | -12.79 |
| 0.5% / 99.5% | -604 | -15.68 |
| 1% / 99% | **-631** | **-16.81** |
| 5% / 95% | -620 | -18.79 |

→ **Effect of winsorization is to make the finding MORE extreme**, not less. This rules out outlier-driven mean.

### Concentration check
- Top 30 most extreme negative CARs use **24 unique gvkeys** (not 1-2 dominant firms)
- Most-frequent gvkey in top-30 appears only twice → no single firm dominates

### Concentration by event date
Mean Healthcare 6m CAR per event (5 most-negative dates):
| Event date | Mean CAR (bp) | n firms | Sign |
|---|---|---|---|
| 2021-07-01 | -1,650 | 483 | EASE (z_innov=-1.78) |
| 2020-10-01 | -1,469 | 485 | EASE (z_innov=-2.14) |
| 2021-01-01 | -1,421 | 485 | EASE (z_innov=-2.45) |
| 2009-04-01 | -1,155 | 489 | EASE (z_innov=-1.44) |
| 2011-10-01 | -1,148 | 489 | TIGHTEN (z_innov=+1.09) |

→ **4 of 5 most-negative-Healthcare-6m events are EASE shocks**. This is consistent with the Day 5 sign-asymmetry table:
- Healthcare 6m × tighten: t = -6.19
- Healthcare 6m × ease: **t = -10.88**

The easing-side pattern is roughly 2× stronger than the tightening-side pattern, both negative.

## Interpretation
Healthcare 6m underperformance after SLOOS shocks reflects a **risk-on rotation**: when banks unexpectedly ease (or unexpectedly tighten less), risk appetite rises, defensive sectors (Healthcare classically defensive) lose relative bid, and cyclical sectors (Industrials, Cons Disc, Materials) attract flows. The 6m horizon captures the full rotation rather than the immediate shock impact (1m: Healthcare = +83bp t=+3.36, the immediate flight-to-quality).

## Actions taken
1. Paper v1 §10 limitation #2 can be downgraded to "confirmed robust" (no more outlier concern).
2. Sign-asymmetry sub-portfolio analysis (paper §9) has additional robustness: the sign-conditional Healthcare short would specifically target ease-shock 6m windows.
3. No code changes needed — the finding stands.

## Tests
No new tests required (existing Layer A integration test already locks the 18/33 cell pass count at the full-sample mean, which would shift if the finding were outlier-driven).
