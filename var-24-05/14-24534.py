def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]
ans = []
for x in range(1,11501):
    num = 7**278 + 7**170 + 7**70 - x
    num = convert(num,7)
    if num.count('0') >= 211:
        ans.append(x)

print(ans)