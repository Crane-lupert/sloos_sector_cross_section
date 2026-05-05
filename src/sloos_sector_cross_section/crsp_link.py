"""CRSP↔Compustat link via CUSIP8 join (Phase 3 honest revision).

The proper time-varying link table `comp.ccmxpf_lnkhist` (or
`crsp_a_ccm.ccmxpf_lnkhist`) is USAGE-blocked in our WRDS subscription
(see `E:/wrds-data-courier/outbox/S1-ccmxpf-lnkhist-blocked-20260505-140255.json`).

Courier-recommended alternative is a CUSIP8 join via existing tables:
  crsp_a_stock.dsenames.cusip ↔ comp_na_daily_all.names.cusip

On our R3000 universe (2,898 gvkeys), this gives 95.4% permno coverage
(2,765 firms), 1-to-1 mapping, no ambiguity.

LIMITATION: static link only. CUSIP changes / spinoffs / mergers that
cause permno↔gvkey reassignment are not tracked. Paper §11 limitation.
When `ccmxpf_lnkhist` is unblocked, swap to time-varying link and
re-validate.
"""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from .wrds_courier_adapter import query

logger = logging.getLogger(__name__)


def build_cusip8_link(gvkeys: list[str] | None = None) -> pd.DataFrame:
    """Build permno↔gvkey link via CUSIP8 SUBSTR.

    Args:
        gvkeys: optional whitelist to restrict the join. Otherwise pulls all.

    Returns:
        DataFrame with columns [permno, gvkey, cusip8, conm, tic].
    """
    base_sql = """
        SELECT
            d.permno,
            n.gvkey,
            SUBSTR(d.cusip, 1, 8) AS cusip8,
            n.conm,
            n.tic
        FROM crsp_a_stock.dsenames d
        INNER JOIN comp_na_daily_all.names n
          ON SUBSTR(d.cusip, 1, 8) = SUBSTR(n.cusip, 1, 8)
        WHERE d.cusip IS NOT NULL AND n.cusip IS NOT NULL
    """
    if gvkeys:
        quoted = ",".join(f"'{g}'" for g in gvkeys)
        base_sql += f" AND n.gvkey IN ({quoted})"
    df = query(base_sql)
    # Dedupe (one row may exist for multiple share classes / cusip versions per pair)
    df = df.drop_duplicates(subset=["permno", "gvkey"]).reset_index(drop=True)
    return df


def cache_link(
    universe: pd.DataFrame,
    out_dir: Path = Path("data/cache"),
    save: bool = True,
) -> pd.DataFrame:
    """Build the CCM link restricted to a universe and cache as parquet."""
    gvkeys = universe["gvkey"].dropna().astype(str).unique().tolist()
    logger.info("building CUSIP8 link for %d universe gvkeys...", len(gvkeys))
    link = build_cusip8_link(gvkeys=gvkeys)
    logger.info("link rows: %d, unique permnos: %d, unique gvkeys: %d",
                len(link), link["permno"].nunique(), link["gvkey"].nunique())
    if save:
        out_dir.mkdir(parents=True, exist_ok=True)
        snap = pd.Timestamp.utcnow().tz_localize(None).strftime("%Y-%m-%d")
        out_path = out_dir / f"ccm_link_cusip8_{snap}.parquet"
        link.to_parquet(out_path)
    return link


def link_summary(link: pd.DataFrame, universe: pd.DataFrame | None = None) -> dict:
    """Return coverage stats."""
    n_pairs = int(len(link))
    n_permno = int(link["permno"].nunique())
    n_gvkey = int(link["gvkey"].nunique())
    permno_per_gvkey = link.groupby("gvkey")["permno"].nunique()
    gvkey_per_permno = link.groupby("permno")["gvkey"].nunique()
    out = {
        "n_pairs": n_pairs,
        "n_unique_permnos": n_permno,
        "n_unique_gvkeys": n_gvkey,
        "ambiguity_gvkeys_with_multi_permno": int((permno_per_gvkey > 1).sum()),
        "ambiguity_permnos_with_multi_gvkey": int((gvkey_per_permno > 1).sum()),
    }
    if universe is not None:
        univ_gvkeys = set(universe["gvkey"].dropna().astype(str).unique())
        matched = univ_gvkeys & set(link["gvkey"].astype(str).unique())
        out["universe_gvkeys"] = len(univ_gvkeys)
        out["universe_gvkeys_matched"] = len(matched)
        out["universe_coverage_pct"] = round(len(matched) / max(len(univ_gvkeys), 1) * 100, 1)
    return out


__all__ = [
    "build_cusip8_link",
    "cache_link",
    "link_summary",
]
