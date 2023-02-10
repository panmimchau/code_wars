"""Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char."""


# answer:
def xo(s):
    if s == None:
        return False
    s = s.lower()
    return s.count("x") == s.count("o")


# test:
def test_xo():
    # given
    s = "ooxx"

    # when
    result = xo(s)

    # then
    assert result
