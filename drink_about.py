"""
    Kids drink toddy.
    Teens drink coke.
    Young adults drink beer.
    Adults drink whisky.

Make a function that receive age, and return what they drink.

Rules:

    Children under 14 old.
    Teens under 18 old.
    Young under 21 old.
    Adults have 21 or more.

"""


# answer:
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif 14 <= age <= 17:
        return "drink coke"
    elif 18 <= age <= 20:
        return "drink beer"
    else:
        return "drink whisky"


# test:
def test_people_with_age_drink():
    # given
    age = 13

    # when
    result = people_with_age_drink(age)

    # then
    assert result == "drink toddy"
    assert people_with_age_drink(17) == "drink coke"
    assert people_with_age_drink(20) == "drink beer"
    assert people_with_age_drink(21) == "drink whisky"
