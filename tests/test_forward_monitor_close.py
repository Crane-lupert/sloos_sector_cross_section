"""Forward monitor — gate-aside contract tests (per governance close audit §6).

These tests lock the contract that `forward_monitor.py` is a health-monitoring
module ONLY. It must NEVER:
  - Demote `LAYER_A_LOCKED.md` status
  - Mutate `CLAUDE.md` outcome class statements
  - Raise exceptions on adverse forward results
  - Have a gate flag exposed in the public API

The `is_health_only` field on the report is a hard-coded `True` contract.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from sloos_sector_cross_section import forward_monitor as fm


def test_report_has_is_health_only_field_hardcoded_true():
    """The contract: `is_health_only` is True by default and the API does not
    expose a way to flip it to False. Tests guard against accidental gating.
    """
    rep = fm.ForwardMonitorReport(
        snapshot_date="2026-05-05",
        n_total_events=36,
        n_events_new_since_last=0,
        new_event_dates=[],
        new_events_pending_horizon={},
        layer_a_baseline_n_pass=15,
        layer_a_with_new_events_n_pass=-1,
        delta_pass=0,
        m1_spearman_6m=float("nan"),
        m2_sign_agree_top6=-1,
        m3_ftest_pval_6m=float("nan"),
    )
    assert rep.is_health_only is True
    # The constructor signature must allow zero-arg defaulting; flipping it
    # explicitly is allowed for testing only but is NOT how this is used in
    # production.


def test_classify_health_aligned():
    """3-of-3 aligned metrics → ALIGNED recommendation."""
    rec = fm.classify_health(spearman_6m=0.7, sign_agree_top6=5, ftest_pval_6m=0.001)
    assert rec.startswith("ALIGNED")
    assert "LAYER A LOCKED status maintained" in rec


def test_classify_health_full_reversal_triggers_governance_audit():
    """3-of-3 full reversal → recommendation references separate governance audit,
    NOT auto-demote. The string contract enforces this language."""
    rec = fm.classify_health(spearman_6m=-0.4, sign_agree_top6=0, ftest_pval_6m=0.50)
    assert rec.startswith("FULL REVERSAL")
    assert "separate governance audit" in rec
    assert "NOT auto-demoted" in rec
    assert "meta-harness governance" in rec


def test_classify_health_boundary():
    """Mixed signals (Spearman 0.3 < 0.5 but not negative) → BOUNDARY recommendation,
    LAYER A LOCKED maintained."""
    rec = fm.classify_health(spearman_6m=0.3, sign_agree_top6=3, ftest_pval_6m=0.10)
    assert rec.startswith("BOUNDARY")
    assert "LAYER A LOCKED status maintained" in rec
    assert "gate-aside, health monitoring" in rec


def test_health_thresholds_are_module_constants_not_runtime_args():
    """The thresholds are module-level constants, locked at code level, not
    arguments to `classify_health`. Prevents accidental tuning to demote."""
    assert fm.HEALTH_M1_SPEARMAN_ALIGNED == 0.5
    assert fm.HEALTH_M1_SPEARMAN_REVERSAL == 0.0
    assert fm.HEALTH_M2_SIGN_AGREE_ALIGNED == 4
    assert fm.HEALTH_M2_SIGN_AGREE_REVERSAL == 1
    assert fm.HEALTH_M3_FTEST_PVAL_ALIGNED == 0.05


def test_top6_sectors_for_m2_constant():
    """Top-6 sectors for M-2 sign agreement are locked as the headline 6m cells:
    Cons Disc / Energy / Industrials / Materials / Healthcare / Utilities."""
    assert fm.TOP6_SECTORS_FOR_M2 == (25, 10, 20, 15, 35, 55)


def test_find_new_events_no_overlap():
    """When new shocks panel is identical to baseline, returns empty index."""
    idx = pd.DatetimeIndex(pd.date_range("1990-04-01", periods=10, freq="QS"))
    df = pd.DataFrame({"is_event_start": [True, False] * 5}, index=idx)
    out = fm.find_new_events(df, df)
    assert len(out) == 0


def test_find_new_events_one_new():
    idx_base = pd.DatetimeIndex(pd.date_range("1990-04-01", periods=8, freq="QS"))
    idx_new = pd.DatetimeIndex(pd.date_range("1990-04-01", periods=10, freq="QS"))
    base = pd.DataFrame({"is_event_start": [True] * 8}, index=idx_base)
    new = pd.DataFrame({"is_event_start": [True] * 10}, index=idx_new)
    out = fm.find_new_events(new, base)
    assert len(out) == 2
    assert out[0] == idx_new[8]
    assert out[1] == idx_new[9]


def test_write_audit_template_contains_lock_language(tmp_path: Path):
    """Generated audit skeleton must include lock language confirming
    health-monitoring (NOT gate)."""
    rep = fm.ForwardMonitorReport(
        snapshot_date="2026-08-15",
        n_total_events=37,
        n_events_new_since_last=1,
        new_event_dates=["2026-07-15"],
        new_events_pending_horizon={"6m_pending": ["2026-07-15"]},
        layer_a_baseline_n_pass=15,
        layer_a_with_new_events_n_pass=-1,
        delta_pass=0,
        m1_spearman_6m=float("nan"),
        m2_sign_agree_top6=-1,
        m3_ftest_pval_6m=float("nan"),
        audit_recommendation="NEW-EVENT-DETECTION ONLY",
    )
    p = fm.write_audit_template(rep, nth=1, out_dir=tmp_path)
    text = p.read_text(encoding="utf-8")
    assert "health monitoring" in text
    assert "LAYER A LOCKED — event-study class **maintained**" in text
    assert "is_health_only=True" in text
    assert "governance close §6.4" in text
    # Filename convention
    assert p.name == "2026-08-15-S1-forward-monitor-1-th.md"


def test_close_audit_pointers_present_in_layer_a_locked_md():
    """Lock: LAYER_A_LOCKED.md must reference both the governance close audit
    and the propagation audit so future Claude sessions navigate correctly."""
    p = Path("LAYER_A_LOCKED.md")
    if not p.exists():
        pytest.skip("LAYER_A_LOCKED.md not present in cwd")
    text = p.read_text(encoding="utf-8")
    assert "2026-05-05-S1-governance-close-layer-a-locked-event-study.md" in text
    assert "2026-05-05-S1-close-propagation.md" in text
    assert "LAYER A LOCKED — event-study class" in text


def test_claude_md_status_is_layer_a_locked():
    """Lock: CLAUDE.md must show LAYER A LOCKED — event-study class status."""
    p = Path("CLAUDE.md")
    if not p.exists():
        pytest.skip("CLAUDE.md not present in cwd")
    text = p.read_text(encoding="utf-8")
    assert "LAYER A LOCKED — event-study class" in text
    assert "Macro/Credit pod first" in text
