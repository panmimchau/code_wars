"""In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?"""

# answer: 
def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

# test:
def test_is_valid_walk():
    #given
    walk = ['n','s','n','s','n','s','n','s','n','s']

    #when
    result = is_valid_walk(walk)

    #then
    assert result

 
    
 