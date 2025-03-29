from plates import is_valid


def test_valid():
    assert is_valid("CS50") == "Valid"
    assert is_valid("AA111") == "Valid"


def test_first_num_zero():
    assert is_valid("CS05") == "Invalid: first num is zero"
    assert is_valid("AA0AA") == "Invalid: first num is zero"


def test_has_middle_num():
    assert is_valid("CS50P") == "Invalid: has middle num"


def test_has_special_char():
    assert is_valid("PI3.14") == "Invalid: has special char"
    assert is_valid("CS50?") == "Invalid: has special char"


def test_wrong_size():
    assert is_valid("H") == "Invalid: wrong size"
    assert is_valid("OUTATIME") == "Invalid: wrong size"
