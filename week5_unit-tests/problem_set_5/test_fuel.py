import pytest
from fuel import get_fraction
from fuel import get_tank
from fuel import SpecialException1


def test_big_over_little():
    with pytest.raises(SpecialException1):
        get_fraction("5/4")


def test_non_int():
    with pytest.raises(ValueError):
        get_fraction("cat")
        get_fraction("one")
        get_fraction("4.4/5.5")


def test_bottom_zero():
    with pytest.raises(SpecialException1):
        get_fraction("4/0")


def test_empty():
    assert get_tank(0, 100) == "E"
    assert get_tank(1, 100) == "E"
    assert get_tank(1, 1000) == "E"


def test_full():
    assert get_tank(100, 100) == "F"
    assert get_tank(99, 100) == "F"
    assert get_tank(999, 1000) == "F"


def test_percent():
    assert get_tank(50, 100) == "50.0%"
    assert get_tank(10, 100) == "10.0%"
    assert get_tank(2, 3) == "67.0%"
