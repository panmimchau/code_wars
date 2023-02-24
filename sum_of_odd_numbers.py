"""Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8

"""


# answer:
def row_sum_odd_numbers(n):
    x = n * (n - 1) + 1
    y = x + (n - 1) * 2

    l = []

    if n == 1:
        return 1
    elif n > 1:
        for i in range(x, y + 1, 2):
            l.append(i)

    return sum(l)

    #return n**3, duh


# test:
def test_row_sum_odd_numbers():
    # given
    n = 1

    # when
    result = row_sum_odd_numbers(n)

    # then
    assert result == 1
    assert row_sum_odd_numbers(2) == 8
    assert row_sum_odd_numbers(13) == 2197
