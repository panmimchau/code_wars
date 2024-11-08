"""
In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).

"""


# answer:
def get_count(sentence):
    vowels = vowels = ["a", "e", "i", "o", "u"]
    l = []

    for x in sentence:
        if x in vowels:
            l.append(x)

    return len(l)


# test:
def test_get_count():
    # given
    sentence = "abracadabra"

    # when
    result = get_count(sentence)

    # then
    assert result == 5
    assert get_count("bcdfghjklmnpqrstvwxz y") == 0
    assert get_count("") == 0
