from calculator import square
import pytest


# pytest automates the try/except tedium
# run: $ pytest pytest_calculator.py
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9 # Fails here and doesn't run other tests. Would be good to run all every time
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0


# =====================================
# all tests functions run
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")
