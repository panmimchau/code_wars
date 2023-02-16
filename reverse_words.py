"""Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained."""


# answer:
def reverse_words(text):
    l = text.split(' ')
    l_rev = []
    for i in l:
        l_rev.append(i[::-1])
    return " ".join(l_rev)


# test:
def test_reverse_words():
    # given
    text = "This is an example!"

    # when
    result = reverse_words(text)

    # then
    assert result == "sihT si na !elpmaxe"
