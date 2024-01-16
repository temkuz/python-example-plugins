from typing import Callable, NamedTuple


class MessageNamespace(NamedTuple):
    message: str
    func: Callable
