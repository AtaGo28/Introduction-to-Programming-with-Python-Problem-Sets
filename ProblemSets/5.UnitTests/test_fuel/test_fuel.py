import pytest
from fuel import convert, gauge

def main():
    test_exceptions
    test_logic_convert
    test_logic_gauge

def test_exceptions():
    pytest.raises(ValueError, convert, fraction="x/y")
    pytest.raises(ValueError, convert, fraction="./y")
    pytest.raises(ValueError, convert, fraction="5/4")
    pytest.raises(ZeroDivisionError, convert, fraction="2/0")

def test_logic_convert():
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("1/5") == 20
    assert convert("4/7") == 57
    assert convert("1/90") == 1
    assert convert("1/110") == 1
    assert convert("1/250") == 0
    assert convert("5/6") == 83
    assert convert("0/2") == 0

def test_logic_gauge():
    assert gauge(50) == "50%"
    assert gauge(100) == "F"
    assert gauge(20) == "20%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(83) == "83%"
    assert gauge(99) == "F"


if __name__ == "__main__":
    main()
