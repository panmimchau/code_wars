"""Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them."""

# answer: 
def to_jaden_case(string):
    if string == '':
        return ''
    else:   
        for x in string:
            return ' '.join(x.capitalize() for x in string.split())
        

# test:
def test_to_jaden_case():
    #given
    string = ''

    #when
    result = to_jaden_case(string)

    #then
    assert result == ''
    assert to_jaden_case("How Can Mirrors Be Real If Our Eyes Aren't Real")

 