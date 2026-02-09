def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i *i < num + 1:
        while num % i == 0:
            d += [i]
            num //= i

            