# S1 Bootstrap EOD audit — 2026-05-05

## Bootstrap 6-step status
| Step | Status | Notes |
|---|---|---|
| 1. Repo structure | PASS | CLAUDE.md / .claude/settings.json / pyproject.toml / .gitignore / .env.example / src + tests __init__.py present |
| 2. uv env + deps | PASS | `uv sync` + `uv sync --extra dev` clean. fredapi 0.5.2, pandas 3.0.2, duckdb 1.5.2, statsmodels 0.14.6 etc. |
| 3. FRED auth | PASS | DRTSCILM length=145 (≥140 ✓), first=1990-04-01, last=2026-04-01, last value=8.1 |
| 4. WRDS courier | PASS | open_db OK; 4 schemas present (crsp_a_stock 13.7GB / comp_na_daily_all 6.4GB / tr_ibes 3.0GB / crsp_a_indexes 2.0GB) |
| 5. Scoop re-check #1 | PASS | No direct competitor paper found across 3 queries (SLOOS×sector / Bidder-Krane-Park follow-up / Ferreira 2026 follow-up). Phase 0 #8 trigger NOT activated. |
| 6. Initial commit + manifest | (this audit) | manifest_phase_status.json + openrouter_spend.jsonl + wrds_query_log.jsonl written |

## Naming differences from CLAUDE.md → actual WRDS courier dump
| CLAUDE.md ref | Actual table in courier | Notes |
|---|---|---|
| `comp.secd` | `comp_na_daily_all.sec_dprc` | 159M rows, 1983-12-30 → 2026-05-01. gvkey + iid + datadate + prccd (price close) + ajexdi (adj) + cshoc (shares out) + cshtrd (volume) etc. Full daily price coverage. |
| `comp.security` | `comp_na_daily_all.namesd` | gvkey + iid + tic + cusip + gsubind + gind. Per-security identifiers. |
| `comp.company` | `comp_na_daily_all.company` | Has `gsector` (GICS sector code), `curr_sp500_flag`, `ipodate`, `dldte`. |
| (ticker→gvkey) | `comp_na_daily_all.names` | gvkey + tic + cusip + cik + gsubind + gind + year1/year2 effective range. |

→ `wrds_courier_adapter.py` (Day 1) will alias internal names: `secd → sec_dprc`, `security → namesd` to keep planning vocabulary consistent while pointing at real tables.

## GICS sector coverage check (Phase 0 #2 universe lock pre-flight)
| GICS code | Sector | Compustat firms |
|---|---|---|
| 10 | Energy | 3,280 |
| 15 | Materials | 4,286 |
| 20 | Industrials | 4,911 |
| 25 | Consumer Discretionary | 5,703 |
| 30 | Consumer Staples | 1,711 |
| 35 | Healthcare | 5,061 |
| 40 | Financials | 6,145 |
| 45 | Information Technology | 5,739 |
| 50 | Communication Services | 1,433 |
| 55 | Utilities | 824 |
| 60 | Real Estate | 576 |
| (NA) | (no GICS) | 17,728 |

→ All 11 GICS sectors populated in cross-section. Smallest sector (Real Estate, 576) is per-firm count — for 1990-2026 monthly panel × R3000 ∩ Real Estate, expected per-cell event count is comfortable above F1-1 n_min=50 floor. Final per-cell verdict at Phase 0 Day 3 EOD audit.

## Resource state
- OpenRouter spend: $0.00 / $5.00 cap (scoop re-check used free WebSearch)
- WRDS queries: 6 (verification only; <50 budget effectively unbounded for this project size)
- Wall time spent: ~30min bootstrap window (within ≤30min target)

## Decision
PROCEED to Phase 0 Day 1: SLOOS multi-series fetch + R3000 universe + GICS map + Day 1 EOD audit.

## Open items / risks carried forward
1. **Naming alias layer**: write `wrds_courier_adapter.py` with thin wrappers so downstream code reads `secd` / `security` even though courier exposes `sec_dprc` / `namesd`. Reduces drift if courier renames.
2. **Phase 0 #8 next trigger**: Day 7 (scoop re-check #2) + Day 12 (scoop re-check #3). Monitor specifically for any extension of Bidder-Krane-Park 2026.02 to equity returns.
3. **iShares R3000 holdings CSV cadence**: Day 1 will pull current-day snapshots only (single CSV per ETF). For pre-2010 universe approximation we will rely on Compustat `curr_sp500_flag` + market-cap rank within GICS sector as a backstop, with the understanding that pre-2000 R3000 reconstruction is approximate.
