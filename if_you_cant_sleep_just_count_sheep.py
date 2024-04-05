"""
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
"""


# answer:
def count_sheep(n):
    list = []

    if n == 0:
        return ""
    elif n == 1:
        return "1 sheep..."
    else:
        for n in range(1, n + 1):
            x = "{} sheep...".format(n)

            list.append(x)
    return "".join(list)


# test:
def test_count_sheep():
    # given
    n = 0

    # when
    result = count_sheep(n)

    # then
    assert result == ""
    assert count_sheep(1) == "1 sheep..."
    assert count_sheep(2) == "1 sheep...2 sheep..."
    assert count_sheep(3) == "1 sheep...2 sheep...3 sheep..."
