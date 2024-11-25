from typing import Callable, Generic, Iterable, List, Optional, TypeVar


T = TypeVar("T")
U = TypeVar("U")
B = TypeVar("B")


class Iter(Generic[T]):
    def __init__(self, payload: Iterable[T]) -> None:
        """
        Initialize an Iter instance with the given payload.

        Args:
            payload (Iterable[T]): The payload to be stored in the Iter instance.
        """
        if not isinstance(payload, Iterable):
            raise TypeError("payload of type <{type(payload)}> is not iterable!")
        self._payload = payload

    def map(self, fn: Callable[[T], U]) -> "Iter[U]":
        """
        Apply a function to each item in the payload and return a new Iter instance with the transformed items.

        This api is lazy - it does not transform the items immediately until it materializes.

        Args:
            fn (Callable[[T], U]): The function to apply to each item in the payload.

        Returns:
            Iter[U]: A new Iter instance with the transformed items.
        """
        return Iter(map(fn, self._payload))

    def filter(self, fn: Callable[[T], bool]) -> "Iter[T]":
        """
        Filter the payload using a function and return a new Iter instance with the filtered items.

        This api is lazy - it does not filter the items immediately until it materializes.

        Args:
            fn (Callable[[T], bool]): The function to use for filtering.

        Returns:
            Iter[T]: A new Iter instance with the filtered items.
        """
        return Iter(filter(fn, self._payload))

    def filter_map(self, fn: Callable[[T], Optional[U]]) -> "Iter[U]":
        """
        Filter and map the payload using a function and return a new Iter instance with the filtered and mapped items.

        This api is lazy - it does not filter and map the items immediately until it materializes.

        Args:
            fn (Callable[[T], Optional[U]]): The function to use for filtering and mapping. Any value evaluated as `None` will be filtered out.

        Returns:
            Iter[U]: A new Iter instance with the filtered and mapped items.
        """

        def gen():
            for item in self._payload:
                if (res := fn(item)) is not None:
                    yield res

        return Iter(gen())

    def bind(self, fn: Callable[[T], Iterable[U]]) -> "Iter[U]":
        """
        Apply a function to each item in the payload and return a new Iter instance with the transformed items.

        This api is lazy - it does not transform the items immediately until it materializes.

        Args:
            fn (Callable[[T], Iterable[U]]): The function to apply to each item in the payload.

        Returns:
            Iter[U]: A new Iter instance with the transformed items.
        """

        def _bind(fn: Callable[[T], Iterable[U]]) -> Iterable[U]:
            for obj in self._payload:
                yield from fn(obj)

        return Iter(_bind(fn))

    def fold(self, base: B, fn: Callable[[B, T], B]) -> B:
        """
        Apply a function to each item in the payload and return a new Iter instance with the transformed items.

        This api is lazy - it does not transform the items immediately until it materializes.

        Args:
            base (B): The initial value of the fold.
            fn (Callable[[B, T], B]): The function to apply to each item in the payload.

        Returns:
            B: The final value of the fold.
        """
        res = base
        for obj in self._payload:
            res = fn(res, obj)
        return res

    def inspect(self, fn: Callable[[T], None]) -> "Iter[T]":
        """
        Apply a function to each item in the payload and return a new Iter instance with the transformed items.

        This api is lazy - it does not transform the items immediately until it materializes.

        Args:
            fn (Callable[[T], None]): The function to apply to each item in the payload.

        Returns:
            Iter[T]: A new Iter instance with the transformed items.
        """

        def gen():
            for obj in self._payload:
                fn(obj)
                yield obj

        return Iter(gen())

    def collect(self, into: Callable[[Iterable[T]], U]) -> U:
        """
        Collect the payload into a single value using the provided function.

        This api is eager! It will collect the payload immediately.

        Args:
            into (Callable[[Iterable[T]], U]): The function to use for collecting the payload.

        Returns:
            U: The collected value.
        """
        return into(self._payload)

    def tolist(self) -> List[T]:
        """
        Convenience method, basically `collect(list)`.
        """
        return self.collect(list)
