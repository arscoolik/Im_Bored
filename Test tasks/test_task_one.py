import pytest
from task_one import solve


def test_possible():
    assert solve(4, 46) == "12+34=46"
    assert solve(5, 15) == "1+2+3+4+5=15"
    assert solve(6, 579) == "123+456=579"
    assert solve(3, 15) == "12+3=15"


def test_impossible():
    assert solve(4, 15) == "There is no possible combination"
    assert solve(10, 11) == "There is no possible combination"
    assert solve(8, 16) == "There is no possible combination"
