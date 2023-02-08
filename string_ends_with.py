"""Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string). """

# answer: 
def solution(text, ending):
    return text.endswith(ending)

    
# test:
def test_solution():
    #given
    text = "samurai"
    ending = "ai"

    #when
    result = solution(text, ending)

    #then
    assert result
    assert solution("ninja", "ja")
    assert solution("sensei", "i")

 