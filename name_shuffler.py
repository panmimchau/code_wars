"""
Write a function that returns a string in which firstname is swapped with last name.
"""


# answer:
def name_shuffler(str_):
    x = str_.split()
    x[0], x[1] = x[1], x[0]
    
    return ' '.join(x)


# test:
def test_name_shuffler():
    # given
    str_ = 'john McClane'

    # when
    result = name_shuffler(str_)

    # then
    assert result == "McClane john"
    assert name_shuffler('Mary jeggins') == 'jeggins Mary'
    assert name_shuffler('tom jerry') == 'jerry tom'

