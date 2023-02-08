"""Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0."""

# answer: 
def summation(num):
    return sum(x for x in range(1, num+1))
    
        

# test:
def test_summation():
    #given
    num = 2

    #when
    result = summation(num)

    #then
    assert result == 3
    assert summation(8) == 36

 