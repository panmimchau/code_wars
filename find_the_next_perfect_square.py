"""Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative."""

# answer: 
def find_next_square(sq):

    perf_sq = sq ** (1/2)

    if perf_sq == int(perf_sq):
        return (perf_sq + 1) ** 2
    else:
        return -1

# test:
def test_find_next_square():
    #given
    sq = 121

    #when
    result = find_next_square(sq)

    #then
    assert result == 144
    assert find_next_square(625) == 676

 
    
 