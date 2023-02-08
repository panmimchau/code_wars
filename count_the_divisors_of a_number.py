n = 12

def divisors(n):

    list_of_divisors = []
    
    for x in range(1, n+1):

        if n % x == 0:
            list_of_divisors.append(x)
    

    return len(list_of_divisors)

divisors(n)    

