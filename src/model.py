from typing import NamedTuple


class Button(NamedTuple):
    command: str
    title: str | None = None
    description: str | None = None
