"""As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements."""


# answer:
def gimme(input_array):
    
    l = sorted(input_array)

    for y in range(len(input_array)):
        if l[1] == input_array[y]:
            return y


# test:
def test_gimme():
    # given
    input_array = [2, 3, 1]

    # when
    result = gimme(input_array)

    # then
    assert result == 0
    assert gimme([5, 10, 14]) == 1
