"""Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step (inclusive).

If begin value is greater than the end, function should returns 0"""


# answer:
def sequence_sum(begin_number, end_number, step):
    l = []

    for x in range(begin_number, end_number + 1, step):
        l.append(x)
    return sum(l)


# test:
def test_sequence_sum():
    # given
    begin_number = 2
    end_number = 6
    step = 2

    # when
    result = sequence_sum(begin_number, end_number, step)

    # then
    assert result == 12
