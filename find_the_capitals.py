"""
Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.
Example (Input --> Output)

"CodEWaRs" --> [0,3,4,6]
"""


# answer:
def capitals(word):
    l = []

    for i in range(len(word)):
        if word[i].isupper():
            l.append(i)

    return l


# test:
def test_capitals():
    # given
    word = "CodEWaRs"

    # when
    result = capitals(word)

    # then
    assert result == [0, 3, 4, 6]
