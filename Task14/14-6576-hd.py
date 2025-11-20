num = 283**382 + 9**15 + 2**3

from string import printable

def convert(num, sys):
    res = ''
    while num != 0:
        res += printable[num%sys]
        num //= sys
    return res [::-1]

R = convert(num,14)
b = R.count('b')
print(b)

c = R.count('c')
print(c)

raz = b - c
print(raz)