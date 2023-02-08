"""Given an integral number, determine if it's a square number."""

# answer: 
def is_square(n):

    perf_square = n ** (1/2)

    if  n < 0:
        return False
    elif perf_square == int(perf_square):
        return True
    else:
        return False
    

# test:
def test_is_square():
    #given
    n = 0

    #when
    result = is_square(n)

    #then
    assert result
    assert is_square(4)
    assert is_square(25)
 
def test_is_not_square():
    assert not is_square(3)
    assert not is_square(26)
    
 