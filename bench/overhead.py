from functools import reduce
import time
from typing import Callable, List
from iterr import Iter
from random import random, seed

"""
Problem statement:

given 1_000_000 randomly generated numbers from 0 to 100:

1. filter out anything that's less than 60.
2. for each number that's left, multiple it by 2.
3. then filter out anything that's divisible by 3.
3. duplicate each number twice in the list.

"""


def time_func(f: Callable):
    def wrapped(*args, **kwargs):
        t1 = time.perf_counter()
        res = f(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"time taken for function {f.__name__} to run: {(t2-t1):.4f} seconds")
        return res

    return wrapped


@time_func
def native(numbers: List[int]):
    result = []
    for number in numbers:
        if number < 60:
            continue
        res = number * 2
        if res % 3 == 0:
            continue
        result.extend([res, res])

    return result


@time_func
def map_filter(numbers: List[int]):
    filtered = filter(lambda x: x > 60, numbers)
    mapped = map(lambda x: x * 2, filtered)
    filtered2 = filter(lambda x: x % 3 != 0, mapped)
    res = []
    for x in filtered2:
        res.extend([x, x])


@time_func
def iterr(numbers: List[int]):
    return (
        Iter(numbers)
        .filter(lambda x: x > 60)
        .map(lambda x: x * 2)
        .map(lambda x: x % 3 != 0)
        .bind(lambda x: [x, x])
        .tolist()
    )


@time_func
def iterr_with_predefined(numbers: List[int]):
    return (
        Iter(numbers)
        .filter(lambda x: x > 60)
        .map(lambda x: x * 2)
        .map(lambda x: x % 3 != 0)
        .bind(lambda x: [x, x])
        .tolist()
    )


if __name__ == "__main__":
    seed("iterr2024")

    numbers = [int(random() * 100) for _ in range(1_000_000)]

    native(numbers)
    map_filter(numbers)
    iterr(numbers)
