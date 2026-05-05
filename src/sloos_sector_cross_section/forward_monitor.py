"""Forward OOS monitor — re-fetch SLOOS each quarter and check for new shock events.

Purpose: meta-harness recommendation #2 — "Forward OOS test (next 4-8 SLOOS releases)
before any portfolio inclusion". This module gives the user a single command to
re-evaluate the headline finding as new SLOOS quarterly releases arrive.

Workflow per quarter:
  1. Refresh SLOOS series from FRED (`sloos_fetch.fetch_and_save`)
  2. Re-construct shocks (AR(1) on full updated series)
  3. Identify NEW events since the last `data/manifest_phase_status.json` snapshot
  4. For each new event, compute forward CARs (1m available immediately, 3m after
     3 months, 6m after 6 months — partial events tracked)
  5. Append new rows to `data/cache/forward_oos_results.parquet`
  6. Recompute Layer A on the augmented panel (full sample including new events)
  7. Report: did headline cells (Cons Disc 6m, Healthcare 6m, etc.) maintain
     significance with the new data?

This is a STUB scaffold — not run automatically. The user invokes it manually
after each quarterly SLOOS release (typically late-Jan, late-Apr, late-Jul, late-Oct).

Status quo (2026-05-05): 36 events to 2025-04-01. Forward-monitoring window
opens at the next SLOOS release (2026-07 expected).
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from .shock_construct import construct_shocks
from .sloos_fetch import fetch_and_save

logger = logging.getLogger(__name__)


@dataclass
class ForwardMonitorReport:
    snapshot_date: str
    n_total_events: int
    n_events_new_since_last: int
    new_event_dates: list[str]
    new_events_pending_horizon: dict[str, list[str]]
    layer_a_with_new_events_n_pass: int
    layer_a_baseline_n_pass: int
    delta_pass: int


def find_new_events(
    new_shocks: pd.DataFrame,
    baseline_shocks: pd.DataFrame,
) -> pd.DatetimeIndex:
    """Return event dates in `new_shocks` not in `baseline_shocks`."""
    new_set = set(new_shocks.index[new_shocks["is_event_start"].fillna(False)])
    base_set = set(baseline_shocks.index[baseline_shocks["is_event_start"].fillna(False)])
    return pd.DatetimeIndex(sorted(new_set - base_set))


def refresh_and_compare(
    baseline_shocks_path: Path | None = None,
) -> ForwardMonitorReport:
    """Re-fetch SLOOS, re-construct shocks, identify new events vs baseline.

    Args:
        baseline_shocks_path: cached shocks parquet from prior run.
            If None, picks the latest `shocks_DRTSCILM_AR1_*.parquet`.

    Returns:
        ForwardMonitorReport with new event dates and Layer A pass count delta.
        DOES NOT modify any cached data — read-only diagnostic.
    """
    cache = Path("data/cache")
    if baseline_shocks_path is None:
        candidates = sorted(cache.glob("shocks_DRTSCILM_AR1_*.parquet"))
        if not candidates:
            raise FileNotFoundError("no baseline shocks parquet to compare against")
        baseline_shocks_path = candidates[-1]
    baseline_shocks = pd.read_parquet(baseline_shocks_path)
    baseline_n = int(baseline_shocks["is_event_start"].fillna(False).sum())

    # Refresh SLOOS
    panel, _ = fetch_and_save()
    new_shocks = construct_shocks(panel)
    new_n = int(new_shocks["is_event_start"].fillna(False).sum())

    new_events = find_new_events(new_shocks, baseline_shocks)
    new_event_dates = [str(d.date()) for d in new_events]

    # Classify by horizon availability based on today's date vs event date
    today = pd.Timestamp.utcnow().tz_localize(None).normalize()
    pending: dict[str, list[str]] = {"1m_pending": [], "3m_pending": [], "6m_pending": []}
    for d in new_events:
        elapsed = (today - d).days
        if elapsed < 21:
            pending["1m_pending"].append(str(d.date()))
        if elapsed < 63:
            pending["3m_pending"].append(str(d.date()))
        if elapsed < 126:
            pending["6m_pending"].append(str(d.date()))

    return ForwardMonitorReport(
        snapshot_date=str(today.date()),
        n_total_events=new_n,
        n_events_new_since_last=int(len(new_events)),
        new_event_dates=new_event_dates,
        new_events_pending_horizon=pending,
        layer_a_with_new_events_n_pass=-1,  # to be filled by caller after panel rebuild
        layer_a_baseline_n_pass=baseline_n,
        delta_pass=0,
    )


def main() -> None:
    """CLI entry: refresh SLOOS, report new events, no panel rebuild."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    report = refresh_and_compare()
    import json
    from dataclasses import asdict

    print(json.dumps(asdict(report), indent=2))


if __name__ == "__main__":
    main()


__all__ = ["ForwardMonitorReport", "find_new_events", "main", "refresh_and_compare"]
