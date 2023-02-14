"""In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows."""


# answer:
def solve(s):
    l_lower = []
    l_upper = []
    l_num = []
    l_other = []
    l = []

    for x in s:
        if x.islower():
            l_lower.append(x)

        elif x.isupper():
            l_upper.append(x)

        elif x.isnumeric():
            l_num.append(x)

        else:
            l_other.append(x)

    l.append(len(l_upper))
    l.append(len(l_lower))
    l.append(len(l_num))
    l.append(len(l_other))

    return l


# test:
def test_solve():
    # given
    s = "*'&ABCDabcde12345"

    # when
    result = solve(s)

    # then
    assert result == [4, 5, 5, 3]
    assert solve("bgA5<1d-tOwUZTS8yQ") == [7, 6, 3, 2]
    assert solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H") == [9, 9, 6, 9]
