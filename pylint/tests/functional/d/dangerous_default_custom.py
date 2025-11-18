"""Extra coverage for dangerous-default-value improvements."""

from __future__ import annotations


class CustomBuffer:
    def __init__(self):
        self.items: list[int] = []

    def append(self, value: int) -> None:
        self.items.append(value)


def mutate_custom(buffer: CustomBuffer = CustomBuffer()):  # [dangerous-default-value]
    buffer.append(1)
    return buffer


def untouched_custom(buffer: CustomBuffer = CustomBuffer()):
    return buffer  # should not trigger


