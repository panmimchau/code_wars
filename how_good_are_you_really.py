"""
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!
"""


# answer:
def better_than_average(class_points, your_points):
    average_points = sum(class_points) / len(class_points)

    if average_points < your_points:
        return True
    else:
        return False


# test:
def test_better_than_average():
    # given
    class_points = [2, 3]
    your_points = 5

    # when
    result = better_than_average(class_points, your_points)

    # then
    assert result == True
    assert better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75) == True
    assert better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50) == False
    assert better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21) == False
