def to_int(num, sys):
    num = num[::-1]
    res = 0
    for i in range(len(num)):
        res += int(num[i], 36)*sys**i
    return res

u = 100_000
for p in range(33, 100):
    num1 = to_int('KOT', p)
    num2 = to_int('GOLODNI', p)
    num3 = to_int('MEEOW', p)
    num4 = to_int('100', p)
    num5 = 20194023088
    if num1 + num2 == num3 * num4 - num5:
        u = min(u, p)
print(to_int('PURR', u))