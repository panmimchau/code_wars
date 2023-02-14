"""Americans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor (due to superstition).

Write a function that given a floor in the american system returns the floor in the european system.

With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 13, they move down by two because there are two omitted numbers below them.

Basements (negatives) stay the same as the universal level."""


# answer:
def get_real_floor(n):
    if n <= 0:
        return n
    elif n in range(1, 13):
        return n - 1
    elif n > 13:
        return n - 2


# test:
def test_get_real_floor():
    # given
    n = 1

    # when
    result = get_real_floor(n)

    # then
    assert result == 0
    assert get_real_floor(5) == 4
    assert get_real_floor(15) == 13
