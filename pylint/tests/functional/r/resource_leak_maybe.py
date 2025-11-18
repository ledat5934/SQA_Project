"""Tests for resource-leak-maybe."""

from __future__ import annotations

import tempfile


def leak_file_system():
    handle = open("foo.txt", encoding="utf-8")  # [resource-leak-maybe, consider-using-with]
    handle.write("boom")
    return handle


def leak_named_temp():
    tmp = tempfile.NamedTemporaryFile(mode="w")  # [resource-leak-maybe, consider-using-with]
    tmp.write("tmp")
    return tmp


def manual_close():
    handle = open("bar.txt", encoding="utf-8")  # [consider-using-with]
    handle.write("ok")
    handle.close()


