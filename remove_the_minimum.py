"""iven an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left."""

# answer: 
def remove_smallest(numbers):

    numbers2 = numbers.copy()

    if len(numbers2) == 0:
        return []
    else:    
        min_num = min(numbers2)
        numbers2.remove(min_num)
        return numbers2

# test:
def test_remove_smallest():
    #given
    numbers = [1,2,3,4,5]

    #when
    result = remove_smallest(numbers)

    #then
    assert result == [2,3,4,5]
    assert remove_smallest([5,3,2,1,4]) == [5,3,2,4]
    assert remove_smallest([2,2,1,2,1]) == [2,2,2,1]


 
    
 