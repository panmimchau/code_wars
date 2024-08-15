"""
Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).
"""


# answer:
def powers_of_two(n):
    l = []
    for x in range(n + 1):
        l.append(2**x)
    return l


# test:
def test_powers_of_two():
    # given
    n = 4

    # when
    result = powers_of_two(n)

    # then
    assert result == [1, 2, 4, 8, 16]
    assert powers_of_two(0) == [1]
    assert powers_of_two(1) == [1, 2]
