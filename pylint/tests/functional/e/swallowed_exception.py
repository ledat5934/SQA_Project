"""Tests for swallowed-exception and empty-except-body warnings."""

from __future__ import annotations

import logging


def swallow_exception():
    try:
        raise ValueError("boom")
    except Exception:  # [swallowed-exception, empty-except-body]
        pass


def empty_handler():
    try:
        raise RuntimeError()
    except ValueError:  # [empty-except-body]
        pass


def debug_only():
    try:
        1 / 0
    except Exception:  # [swallowed-exception, empty-except-body]
        logging.debug("ignored: %s", "boom")


def meaningful_handler():
    try:
        1 / 0
    except Exception:
        logging.warning("handled properly")


