from bank import value


def test_100():
    assert value("not and h") == "$100"
    assert value("") == "$100"
    assert value("123") == "$100"


def test_20():
    assert value("hey") == "$20"
    assert value("ho") == "$20"
    assert value("howdy") == "$20"


def test_0():
    assert value("hello") == "$0"
    assert value("hello how are you") == "$0"


def test_nothing():
    assert value() == "$100"


def test_silent():
    assert value("") == "$100"


def test_blank():
    assert value(" ") == "$100"
