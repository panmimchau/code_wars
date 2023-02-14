"""Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array."""


# answer:
def solution(nums):
    if nums == None or nums == []:
        return []
    else:
        nums.sort()
        return nums


# test:
def test_solution():
    # given
    nums = [1, 2, 3, 10, 5]

    # when
    result = solution(nums)

    # then
    assert result == [1, 2, 3, 5, 10]
    assert solution(None) == []
    assert solution([2, 20, 10]) == [2, 10, 20]
