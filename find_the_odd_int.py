


# answer:
def find_it(seq):
    for x in seq:
        if seq.count(x) % 2 != 0:
            return x


# test:
def test_find_it():
    # given
    seq = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]

    # when
    result = find_it(seq)

    # then
    assert result == 5
