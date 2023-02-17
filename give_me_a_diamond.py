"""You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size."""


# answer: (with help form github :] )
n = 9


def diamond(n):
    if n % 2 == 0 or not str(n).isdigit():
        return None

    expected = "".join(create_star(1, n, 2, n))

    expected += "".join(create_star(n, 0, -2, n))
    return expected


def create_star(start, finish, by, total):
    return [" " * ((total - i) // 2) + "*" * i + "\n" for i in range(start, finish, by)]


# test:
def test_diamond():
    # given
    n = 5

    # when
    result = diamond(n)

    # then
    assert result == "  *\n ***\n*****\n ***\n  *\n"
    assert diamond(1) == "*\n"
