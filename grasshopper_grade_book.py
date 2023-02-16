"""Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade."""


# answer:
def get_grade(s1, s2, s3):
    avr_score = int((s1 + s2 + s3) / 3)

    if avr_score in range(90, 101):
        return "A"
    elif avr_score in range(80, 90):
        return "B"
    elif avr_score in range(70, 80):
        return "C"
    elif avr_score in range(60, 70):
        return "D"
    elif avr_score in range(0, 60):
        return "F"


# test:
def test_get_grade():
    # given
    s1 = 95
    s2 = 90
    s3 = 93

    # when
    result = get_grade(s1, s2, s3)

    # then
    assert result == "A"
