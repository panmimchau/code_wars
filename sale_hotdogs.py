"""
Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accepts 1 parameter:n, n is the number of hotdogs a customer will buy, different numbers have different prices (refer to the following table), return how much money will the customer spend to buy that number of hotdogs.
number of hotdogs 	price per unit (cents)
n < 5 	100
n >= 5 and n < 10 	95
n >= 10 	90

You can use if..else or ternary operator to complete it.
"""


# answer:
def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif n >= 5 and n < 10:
        return n * 95
    else:
        return n * 90


# test:
def test_sale_hotdogs():
    # given
    n = 1

    # when
    result = sale_hotdogs(n)

    # then
    assert result == 100
    assert sale_hotdogs(2) == 200
    assert sale_hotdogs(11) == 990
    assert sale_hotdogs(5) == 475
    
