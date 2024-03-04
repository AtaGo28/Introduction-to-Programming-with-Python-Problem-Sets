from um import count

def main():
    test_count
    test_case
    test_words
    
def test_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um") == 1
    
def test_case():
    assert count("Um, thanks, um...") == 2
    assert count("Um, hello, um, world, um... Um...") == 4
    
def test_words():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, yummy") == 1
    assert count("Mummy") == 0
    
if __name__ == "__main":
    main()