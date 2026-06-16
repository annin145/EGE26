def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i**2 <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d
#
def is_prime(num):
    if num < 2: return False
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            return False
    return True
#
def divs(num):
    d = set()
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            d |= {i,num//i}
    return d
#
def prime_divs(num):
    d = set()
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            if is_prime(i):
                d |= {i}
            if is_prime(num//i):
                d |= {num//i}
    return d
