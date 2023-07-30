from utils import arrs
from utils.arrs import my_slice


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

def test_my_slice():
    assert my_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]
    assert my_slice([1, 2, 3, 4, 5], -3, None) == [3, 4, 5]
    assert my_slice([], 0, 10) == []
    assert my_slice([1, 2, 3, 4, 5], -10, 3) == [1, 2, 3]
