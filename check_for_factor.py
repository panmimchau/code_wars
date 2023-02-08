"""This function should test if the factor is a factor of base."""

# answer: 
def check_for_factor(base: int, factor: int) -> bool: 
    return base % factor == 0

# test:
def test_check_for_factor():
    #given
    base = 10
    factor = 2

    #when
    result = check_for_factor(base, factor)

    #then
    assert result
    assert check_for_factor(10, 2)
    assert check_for_factor(63, 7)
    assert check_for_factor(2450, 5)
 