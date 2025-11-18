"""Example avoiding swallowed-exception."""

from __future__ import annotations

import logging


def handle_exception():
    try:
        raise RuntimeError("boom")
    except Exception as exc:
        logging.error("Processing failed: %s", exc)
        raise

