"""
Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
Examples

"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"

    don't worry about uppercase vowels
    y is not considered a vowel for this kata

"""


# answer:
def shortcut(s):
    lc_vowels = ["a", "e", "i", "o", "u"]
    l = list(s)

    for x in s:
        for y in lc_vowels:
            if x == y and s.count(x) > 0:
                l.remove(x)

    return "".join(l)


# test:
def test_shortcut():
    # given
    s = "how are you today?"

    # when
    result = shortcut(s)

    # then
    assert result == "hw r y tdy?"
    assert shortcut("hellooooo") == "hll"
    assert shortcut("complain") == "cmpln"
