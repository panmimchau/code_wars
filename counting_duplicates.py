"""Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits."""

# answer: 
def duplicate_count(text):

    l = list(text.lower())
    l_duplicates = []


    for x in l:
        if l.count(x) > 1:
            l_duplicates.append(x)

    return len(set(l_duplicates))     

# test:
def test_duplicate_count():
    #given
    text = "abcde"

    #when
    result = duplicate_count(text)

    #then
    assert result == 0
    assert duplicate_count("aabbcde") == 2
    assert duplicate_count("Indivisibilities") == 2
    assert duplicate_count("aA11") == 2
    
 