from seasons import minutes, text_minutes

def main():
    test_minutes()
    test_text_minutes()
    
def test_minutes():
    assert minutes(2023, 2, 22) == 525600
    assert minutes(2022, 2, 22) == 1051200
    assert minutes(2023, 22, 2) == "Invalid date"
    assert minutes(1997, "march", 17) == "Invalid date"
    
def test_text_minutes():
    assert text_minutes(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert text_minutes(1051200) == "One million, fifty-one thousand, two hundred minutes"
    
if __name__ == "__main__":
    main()