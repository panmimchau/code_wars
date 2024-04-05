"""
Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.

For example, if this array were passed as an argument:

["Telescopes", "Glasses", "Eyes", "Monocles"]

Your function would return the following array:

["Eyes", "Glasses", "Monocles", "Telescopes"]

All of the strings in the array passed to your function will be different lengths, so you will not have to decide how to order multiple strings of the same length.
"""


# answer:
def sort_by_length(arr):
    arr.sort(key=len)
    return arr


# test:
def test_sort_by_length():
    # given
    arr = ["beg", "life", "i", "to"]

    # when
    result = sort_by_length(arr)

    # then
    assert result == ["i", "to", "beg", "life"]
    assert sort_by_length(["", "moderately", "brains", "pizza"]) == [
        "",
        "pizza",
        "brains",
        "moderately",
    ]
    assert sort_by_length(["", "dictionary", "eloquent", "bees"]) == [
        "",
        "bees",
        "eloquent",
        "dictionary",
    ]
    assert sort_by_length(
        ["a longer sentence", "the longest sentence", "a short sentence"]
    ) == ["a short sentence", "a longer sentence", "the longest sentence"]
