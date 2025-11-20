num = 729**8 - 3**18 + 85

cnt_9 = 0
while num:
    if num % 9 == 0:
        cnt_9 +=1
    num //= 9

print(cnt_9)