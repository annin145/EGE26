from string import printable
def convert(num,sys):
    res = ''
    while num != 0:
        res += printable[num%sys]
        num //= sys
    return res[::-1]

ans = []
for x in range(1,2031):
    num = 7**170 + 7**100 - x
    num7 = convert(num, 7)
    cnt = num7.count('0')
    ans.append([cnt, x])
print(max(ans))