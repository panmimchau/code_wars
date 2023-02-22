"""Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them."""


# answer:
def between(a, b):
    l = []

    for x in range(a, b + 1):
        l.append(x)
    return l


# test:
def test_between():
    # given
    a = 1
    b = 4

    # when
    result = between(a, b)

    # then
    assert result == [1, 2, 3, 4]
