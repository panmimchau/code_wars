"""
Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).
Examples

count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]

"""

# answer:


def count_by(x, n):
    l = []

    for i in range(x, (n * x) + x, x):
        l.append(i)

    return l


# test:
def test_count_by():
    # given
    x = 2
    n = 5

    # when
    result = count_by(x, n)

    # then
    assert result == [2, 4, 6, 8, 10]
    assert count_by(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert count_by(100, 5) == [100, 200, 300, 400, 500]
