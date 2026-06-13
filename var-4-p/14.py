cnt = 0
ans = 0
for x in range(1,9430):
    num = 39**483 + 39**235 - x
    while num:
        if num % 39 == 0:
            cnt += 1
            num //= 39
        ans = max(ans,cnt)

print(ans)