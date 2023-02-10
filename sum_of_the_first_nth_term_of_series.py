"""Task:

Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

Rules:

    You need to round the answer to 2 decimal places and return it as String.

    If the given value is 0 then it should return 0.00

    You will only be given Natural Numbers as arguments.
"""


# answer:
def series_sum(n):
    fractions = []
    for n in range(1, 3 * n - 1, 3):
        fractions.append(1 / n)
    return "{:.2f}".format(sum(fractions))


# test:
def test_series_sum():
    # given
    n = 2

    # when
    result = series_sum(n)

    # then
    assert result == "1.25"
    assert series_sum(1) == "1.00"
    assert series_sum(3) == "1.39"
