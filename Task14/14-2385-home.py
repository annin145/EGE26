num =16**820 - 2**761 + 14

cnt_4 = 0
while num :
    if num % 4 == 0:
        cnt_4 +=1
    num //= 4

print(cnt_4)

# 378