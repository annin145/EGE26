def convert(num,sys):
    res = ''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res [::-1]
ans = []
cnt = 0
for x in range(10,70001):
    num = 5**2025 + 5**400 - x
    num5 = convert(num,5)
    for i in num5:
        if i == 4:
           cnt +=1
           ans.append(cnt,x)

print(max(ans))
