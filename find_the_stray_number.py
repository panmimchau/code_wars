"""
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)
Examples

[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
"""

# answer:


def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x


# test:
def test_stray():
    # given
    arr = [17, 17, 3, 17, 17, 17, 17]

    # when
    result = stray(arr)

    # then
    assert result == 3
    assert stray([1, 1, 2]) == 2
