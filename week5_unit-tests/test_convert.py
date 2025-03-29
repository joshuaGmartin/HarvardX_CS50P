import pytest
from convert import convert


def test_int():
    assert convert(1) == 149597870700.0
    assert convert(0) == 0
    assert convert(-1) == -149597870700.0
    assert convert(2) == 299195741400.0


def test_error():
    with pytest.raises(TypeError):
        convert("cat")
        convert("1")


# test floats with tolerance
def test_float():
    # assert convert(0.001) == pytest.approx(149597870.7, abs=0.1)
    # assert convert(0.001) == pytest.approx(149597870.7, abs=1e-7)
    assert convert(0.001) == pytest.approx(149597870.7, abs=1e-8)  # Fails on tolerance
