from string import printable
def convert(num,sys):
    res = ''
    while num != 0:
        res += printable[num%sys]
        num //= sys
    return res [::-1]


ans = []
for x in range(1, 27_000):
    num = 3*27**9 + 2*27**6 + 27**3 - x
    num27 = convert(num, 27)
    if num27.count('0') == 6:
        ans.append(x)

print(min(ans))