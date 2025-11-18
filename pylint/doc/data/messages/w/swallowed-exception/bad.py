"""Example triggering swallowed-exception."""

from __future__ import annotations


def swallow_everything():
    try:
        raise RuntimeError("boom")
    except Exception:  # [swallowed-exception]
        pass

