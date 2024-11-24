from typing import Set
from iterr import Iter
import pytest


@pytest.fixture
def iterints() -> Iter[int]:
    return Iter(range(10))


def test_map(iterints: Iter[int]):
    assert iterints.map(lambda x: x + 1).tolist() == list(range(1, 11))


def test_filter(iterints: Iter[int]):
    assert iterints.filter(lambda x: x % 2 == 0).tolist() == [0, 2, 4, 6, 8]


def test_bind(iterints: Iter[int]):
    assert len(iterints.bind(lambda x: [x, x]).tolist()) == 20


def test_fold(iterints: Iter[int]):
    assert iterints.fold(0, lambda acc, num: acc + num) == sum(range(10))


def test_collect(iterints: Iter[int]):
    intset = iterints.collect(set)
    assert isinstance(intset, Set)
    assert len(intset) == 10
