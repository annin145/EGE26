from string import printable
def convert(num,sys):
    res = ''
    while num != 0:
        res += printable[num%sys]
        num //= sys
    return res[::-1]

num = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025
num = convert(num, 25)
cnt = num.count('0')
print(cnt)