"""The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate."""


# answer:
def duplicate_encode(word):
    
    l = []
    l_new = []

    for x in word.lower():
       l.append(x)
    print(l)

    for i in l:
        if l.count(i) == 1:
            l_new.append('(')
        elif l.count(i) > 1:
            l_new.append(')')

    return ''.join(l_new)


# test:
def test_duplicate_encode():
    # given
    word = "din"

    # when
    result = duplicate_encode(word)

    # then
    assert result == "((("
    assert duplicate_encode("recede") == "()()()"
