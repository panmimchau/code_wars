"""Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?

Examples:

input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.

Input may be any positive or negative integer (including 0).

You can assume that all inputs are valid integers.
"""


# answer:
def round_to_next5(n):
    if n % 5 == 0:
        return n
    elif n > 0 and n // 5 * 5 < n:
        return (n // 5 * 5) + 5
    elif n < 0 and n // 5 * 5 < n:
        return (n // 5 * 5) + 5


# test:
def test_to_next5():
    # given
    n = 2

    # when
    result = round_to_next5(n)

    # then
    assert result == 5
    assert round_to_next5(-2) == 0
    assert round_to_next5(12) == 15
