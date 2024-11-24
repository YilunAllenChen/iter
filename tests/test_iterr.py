from iterr import Iter


def test_basic():
    assert Iter([1, 2, 3]).map(lambda x: x + 1).tolist() == [2, 3, 4]
