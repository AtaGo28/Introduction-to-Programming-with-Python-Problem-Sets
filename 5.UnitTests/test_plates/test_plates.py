from plates import is_valid

def main():
    test_numstart()
    test_lenght()
    test_logic()
    test_isalpha()

def test_numstart():
    assert is_valid("cs50") == True
    assert is_valid("50cs") == False
    assert is_valid("cs50p") == False
    assert is_valid("c500") == False

def test_lenght():
    assert is_valid("cs") == True
    assert is_valid("c") == False
    assert is_valid("cs5000") == True
    assert is_valid("cs50000") == False

def test_logic():
    assert is_valid("5c") == False
    assert is_valid("c5") == False
    assert is_valid("50") == False
    assert is_valid("5") == False
    assert is_valid("cs500p") == False
    assert is_valid("cs0555") == False

def test_isalpha():
    assert is_valid(" cs") == False
    assert is_valid("cs500.") == False
    assert is_valid("cs.50") == False
    assert is_valid("cs50?,") == False
    assert is_valid("cs555 ") == False
    assert is_valid("/cs555") == False


if __name__ == "__main__":
    main()
