"""Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order."""


# answer:
def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    else:
        l = [item**2 for item in array1]

        return sum(l) == sum(array2) and len(set(l)) == len(set(array2))


# test:
def test_comp():
    # given
    array1 = [121, 144, 19, 161, 19, 144, 19, 11]
    array2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

    # when
    result = comp(array1, array2)

    # then
    assert result
