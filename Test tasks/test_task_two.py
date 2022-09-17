import pytest
from task_two import solve


def test_inc():
    assert solve([1, 2, 3]) == (0, 2)
    assert solve([5, 6, 7, 1, 2, 3, 4, 6, 5, 7, 8]) == (3, 7)
    assert solve([1, 2, 3, 1, 2, 3, 1, 2, 3]) == (0, 2)

def test_decr():
    assert solve([3, 2, 1]) == (0, 2)
    assert solve([5, 6, 7, 5, 4, 3, 2, 1, 5, 7, 8]) == (2, 7)


def test_eq():
    assert solve([0, 0, 0, 0, 0]) == (0, 0)
    assert solve([1, 1, 1, 1, 1]) == (0, 0)
    assert solve([1000]) == (0, 0)