from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("cookie") == "ck"

def test_uppercase():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Cookie") == "Ck"

def test_capitalized():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("COOKIE") == "CK"

def test_numbers():
    assert shorten("tw1tter") == "tw1ttr"
    assert shorten("tw1tt3r") == "tw1tt3r"
    assert shorten("c00kie") == "c00k"
    assert shorten("c00k13") == "c00k13"

def test_punctuation():
    assert shorten("twitter..") == "twttr.."
    assert shorten("cookie..") == "ck.."
    assert shorten("twi.tte.r") == "tw.tt.r"
    assert shorten("co.o.ki.e.") == "c..k.."
