"""Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle"""

# answer: 
def find_needle(haystack):
    for x in haystack:
        if x == 'needle':
            return 'found the needle at position {}'.format(haystack.index('needle'))
    
        

# test:
def test_find_needle():
    #given
    haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

    #when
    result = find_needle(haystack)

    #then
    assert result == "found the needle at position 5"
    assert find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]) == 'found the needle at position 3'

 