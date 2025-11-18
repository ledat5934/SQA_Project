"""Tests for high risk TODO detection."""
# pylint: disable=missing-function-docstring


def do_something():
    """Function with various notes."""

    # +1: [high-risk-todo]
    # TODO!!! this needs immediate attention
    pass


def regular_note():
    # +1: [fixme]
    # TODO: routine improvement
    return None

