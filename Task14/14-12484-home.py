ans = []
for x in range(1, 50):
    for y in range(1, 50):
        num = 5 ** 50 + 5 ** 30 - 5 ** x - y - 5 ** y - x
        if num > 0:
            cnt = 0
            while num > 0:
                if num % 5 == 0:
                    cnt += 1
                num //= 5
            if cnt == 10:
                ans.append(x * y) 
print(max(ans))