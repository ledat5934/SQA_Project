"""Example avoiding resource-leak-maybe."""

from __future__ import annotations


def read_file(path: str):
    with open(path, encoding="utf-8") as handle:
        return handle.read()

