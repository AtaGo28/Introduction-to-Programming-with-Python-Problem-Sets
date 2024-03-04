from working import convert
import pytest


def main():
    test_convert()
    test_convert12()
    test_exceptions()


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_convert12():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:15 AM to 12:30 PM") == "00:15 to 12:30"


def test_exceptions():
    pytest.raises(ValueError, convert, s="9:60 AM to 5:60 PM")
    pytest.raises(ValueError, convert, s="9 AM - 5 PM")
    pytest.raises(ValueError, convert, s="09:00 AM - 17:00 PM")


if __name__ == "__main__":
    main()
