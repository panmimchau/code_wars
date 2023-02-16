"""Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.

a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.

The four operators are "add", "subtract", "divide", "multiply"."""


# answer:
def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b


# test:
def test_arithmetic():
    # given
    a = 5
    b = 2
    operator = "add"

    # when
    result = arithmetic(a, b, operator)

    # then
    assert result == 7
