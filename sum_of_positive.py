"""You get an array of numbers, return the sum of all of the positives ones."""

# answer: 
def positive_sum(arr):
    y = 0
    for x in arr:
        if x >= 0:
            y = y + x
    return y

    
# test:
def test_positive_sum():
    #given
    arr = [1,-4,7,12]

    #when
    result = positive_sum(arr)

    #then
    assert result == 20
    assert positive_sum([]) == 0
    assert positive_sum([1,-2,3,4,5]) == 13

 