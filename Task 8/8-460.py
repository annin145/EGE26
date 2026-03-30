from itertools import product

cnt = set()
for val1 in product('01234', repeat=5):
    val1 = ''.join(val1)
    for val2 in product('01234', repeat=5):
        val2 = ''.join(val2)
        if val1[0] != '0' and val2[0] != '0' and int(val1,5) > int(val2,5):
            cnt |= {int(val1,5) - int(val2,5)}

print(len(cnt))
