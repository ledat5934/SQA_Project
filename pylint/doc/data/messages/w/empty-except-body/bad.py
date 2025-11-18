"""Example triggering empty-except-body."""

from __future__ import annotations


def ignore_value_error():
    try:
        int("bad")
    except ValueError:  # [empty-except-body]
        pass

