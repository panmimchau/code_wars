"""The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}."""

# answer: 
def count(string):
    d = dict()
    for x in string:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    return d

    
# test:
def test_count():
    #given
    string = 'aba'

    #when
    result = count(string)

    #then
    assert result == {'a': 2, 'b': 1}
    assert count('') == {}
    assert count('dupa') == {'a': 1, 'd': 1, 'p': 1, 'u': 1}

 