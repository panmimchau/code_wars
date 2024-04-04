"""
You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.

You can assume all values in the array are numbers.
"""


# answer:
def small_enough(array, limit):
    return all(x <= limit for x in array)


# test:
def test_small_enough():
    # given
    array = [66, 101]
    limit = 200

    # when
    result = small_enough(array, limit)

    # then
    assert result == True
    assert small_enough([101, 45, 75, 105, 99, 107], 107) == True
    assert small_enough([78, 117, 110, 99, 104, 117, 107, 115] ,100) == False
    assert small_enough([1, 1, 1, 1, 1, 2], 1) == False
