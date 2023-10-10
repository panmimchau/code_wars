"""
Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
"""


# answer:
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


# test:
def is_triangle():
    # given
    a = 1
    b = 2
    c = 2

    # when
    result = is_triangle(a, b, c)

    # then
    assert result == True
    assert is_triangle(7, 2, 2) == False
