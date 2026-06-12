def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]
cnt = 0
ans = 10*10
for x in range(0,2031):
    num = 6**2030 + 6**100 - x
    num = convert(num,6)
    for i in num:
        if i == 0:
            cnt +=1
            ans = min(ans,cnt)

print(ans)

