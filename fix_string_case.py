"""
In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

    make as few changes as possible.
    if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.

For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

"""


# answer:
def solve(s):
    upper = []
    lower = []
    for x in s:
        if x.isupper():
            upper.append(x)
        else:
            lower.append(x)

    if len(upper) == len(lower):
        return s.lower()
    elif len(upper) > len(lower):
        return s.upper()
    elif len(upper) < len(lower):
        return s.lower()


# test:
def test_solve():
    # given
    s = "CODe"

    # when
    result = solve(s)

    # then
    assert result == "CODE"
    assert solve("COde") == "code"
    assert solve("Code") == "code"
