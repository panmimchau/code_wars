"""
Write a function that takes a list of strings as an argument and returns a filtered list containing the same elements but with the 'geese' removed.

The geese are any strings in the following array, which is pre-populated in your solution:

  ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

For example, if this array were passed as an argument:

 ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]

Your function would return the following array:

["Mallard", "Hook Bill", "Crested", "Blue Swedish"]

"""


# answer:
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    l = []
    for x in birds:
        if x not in geese:
            l.append(x)

    return l


# test:
def test_goose_filter():
    # given
    birds = [
        "Mallard",
        "Hook Bill",
        "African",
        "Crested",
        "Pilgrim",
        "Toulouse",
        "Blue Swedish",
    ]

    # when
    result = goose_filter(birds)

    # then
    assert result == ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
    assert goose_filter(
        ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
    ) == ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
