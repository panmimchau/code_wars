"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

"""


# answer:
def number(lines):
    l = []

    for i in range(1, len(lines) + 1):
        x = "{}: {}".format(i, lines[i - 1])

        l.append(x)

    return l


# test:
def test_number():
    # given
    lines = ["a", "b", "c"]

    # when
    result = number(lines)

    # then
    assert result == ["1: a", "2: b", "3: c"]
