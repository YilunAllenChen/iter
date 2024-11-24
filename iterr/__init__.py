from typing import Callable, Generic, Iterable, List, TypeVar


T = TypeVar("T")
U = TypeVar("U")
B = TypeVar("B")


class Iter(Generic[T]):
    def __init__(self, payload: Iterable[T]) -> None:
        if not isinstance(payload, Iterable):
            raise TypeError("payload of type <{type(payload)}> is not iterable!")
        self._payload = payload

    def map(self, fn: Callable[[T], U]) -> "Iter[U]":
        return Iter(map(fn, self._payload))

    def filter(self, fn: Callable[[T], bool]) -> "Iter[T]":
        return Iter(filter(fn, self._payload))

    def bind(self, fn: Callable[[T], Iterable[U]]) -> "Iter[U]":
        def _bind(fn: Callable[[T], Iterable[U]]) -> Iterable[U]:
            for obj in self._payload:
                yield from fn(obj)

        return Iter(_bind(fn))

    def fold(self, base: B, fn: Callable[[B, T], B]) -> B:
        res = base
        for obj in self._payload:
            res = fn(res, obj)
        return res

    def inspect(self, fn: Callable[[T], None]) -> "Iter[T]":
        def gen():
            for obj in self._payload:
                fn(obj)
                yield obj

        return Iter(gen())

    def collect(self, into: Callable[[Iterable[T]], U]) -> U:
        return into(self._payload)

    def tolist(self) -> List[T]:
        return self.collect(list)
