from typing import Any


def is_foo(item: Any) -> bool:
    pass


def is_bar(item: Any) -> bool:
    pass


def process_foo(item: Any) -> Any:
    pass


def process_bar(item: Any) -> Any:
    pass


total = 0


def without_enumerate(n_foo: int, n_bar: int, items: list) -> int:
    global total

    for item in items:
        if is_foo(item):
            process_foo(item)
            n_foo += 1
        if is_bar(item):
            process_bar(item)
            n_bar += 1
        else:
            pass
    total += 1
