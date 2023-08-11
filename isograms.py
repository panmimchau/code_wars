"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false


"""

# answer:


def is_isogram(string):
    s = string.lower()

    l = list(s)
    l2 = []

    for x in l:
        if x not in l2:
            l2.append(x)

    return len(l) == len(l2)


# test:
def test_is_isogram():
    # given
    string = "Dermatoglyphics"

    # when
    result = is_isogram(string)

    # then
    assert result == True
    assert is_isogram("moOse") == False
    assert is_isogram("aba") == False
