"""You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters."""

# answer: 
def get_middle(s):

    l = list(s)
    
    middle = len(l) / 2
    print(middle)
    if len(l) % 2 == 0:
        return f'{l[(int(middle) - 1)]}{l[(int(middle))]}'
    else:
        return f'{l[(int(middle))]}'

# test:
def test_get_middle():
    #given
    s = "test"

    #when
    result = get_middle(s)

    #then
    assert result == "es"
    assert get_middle("testing") == "t"
    assert get_middle("middle") == "dd"
    assert get_middle("A") == "A"
    
 