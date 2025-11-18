"""Example triggering resource-leak-maybe."""

from __future__ import annotations


def read_file(path: str):
    handle = open(path, encoding="utf-8")  # [resource-leak-maybe]
    return handle.read()

