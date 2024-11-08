"""
In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).

"""


# answer:
def factorial(n):
    l = []
    res = 1

    if n > 12 or n < 0:
        raise ValueError

    for x in range(1, n + 1):
        l.append(x)

    for val in l:
        res = res * val

    return res


# test:
def test_factorial():
    # given
    n = 3

    # when
    result = factorial(n)

    # then
    assert result == 6
    assert factorial(2) == 2
    assert factorial(7) == 5040
