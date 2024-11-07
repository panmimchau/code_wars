"""
You need to write a function that reverses the words in a given string. Words are always separated by a single space.

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

Example (Input --> Output)

"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"


"""


# answer:
def reverse(st):
    l = st.split()
    l.reverse()

    return " ".join(l)


# test:
def test_reverse():
    # given
    st = "Hello World"

    # when
    result = reverse(st)

    # then
    assert result == "World Hello"
    assert reverse("Hi There.") == "There. Hi"
