"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
Examples (Input --> Output)

"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""


# answer:
def validate_pin(pin):
    x = pin.isdigit()

    if x == True:
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False
    else:
        return False


# test:
def test_validate_pin():
    # given
    pin = "1234"

    # when
    result = validate_pin(pin)

    # then
    assert result == True
    assert validate_pin("098765") == True
    assert validate_pin("a234") == False
    assert validate_pin("pin") == False
