from twttr import twttrize


def test_twttrize():
    assert twttrize("Twitter") == "Twttr"
    assert twttrize("What's your name?") == "Wht's yr nm?"
    assert twttrize("CS50") == "CS50"
