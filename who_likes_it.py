"""You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item."""

# answer: 
def likes(names):
    if names == []:
        return f'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) > 3:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'

    
# test:
def test_likes():
    #given
    names = ['Peter']

    #when
    result = likes(names)

    #then
    assert result == "Peter likes this"
    assert likes([]) == "no one likes this"
    assert likes(["Jacob", "Alex"]) == "Jacob and Alex like this"
    assert likes(["Max", "John", "Mark"]) == "Max, John and Mark like this"
    assert likes(["Alex", "Jacob", "Mark", "Max"]) == "Alex, Jacob and 2 others like this"

 