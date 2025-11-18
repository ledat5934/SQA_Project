"""Example avoiding empty-except-body."""

from __future__ import annotations


def handle_value_error():
    try:
        int("bad")
    except ValueError as exc:
        raise RuntimeError("Conversion failed") from exc

