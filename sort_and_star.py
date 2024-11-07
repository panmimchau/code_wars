"""
You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.

"""


# answer:
def two_sort(array):
    array.sort()
    x = array[0]
    l = list(x)
    return "***".join(l)


# test:
def test_two_sort():
    # given
    array = [
        "bitcoin",
        "take",
        "over",
        "the",
        "world",
        "maybe",
        "who",
        "knows",
        "perhaps",
    ]

    # when
    result = two_sort(array)

    # then
    assert result == "b***i***t***c***o***i***n"
    assert (
        two_sort(
            [
                "turns",
                "out",
                "random",
                "test",
                "cases",
                "are",
                "easier",
                "than",
                "writing",
                "out",
                "basic",
                "ones",
            ]
        )
        == "a***r***e"
    )
