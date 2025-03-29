# Must include __init__.py (blank file) in test folder: tells python to treat folder as package
# allows this to be run: $ pytest test   (tests all in folder)
from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_arg():
    assert hello("bob") == "hello, bob"
