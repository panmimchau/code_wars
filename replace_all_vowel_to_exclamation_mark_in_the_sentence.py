"""
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples

replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"

"""


# answer:
def replace_exclamation(st):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    l = list(st)

    for x in range(len(l)):
        if l[x] in vowels:
            l[x] = "!"
            st = "".join(l)

    return st


# test:
def test_replace_exclamation():
    # given
    st = "Hi!"

    # when
    result = replace_exclamation(st)

    # then
    assert result == "H!!"
    assert replace_exclamation("aeiou") == "!!!!!"
    assert replace_exclamation("ABCDE") == "!BCD!"
