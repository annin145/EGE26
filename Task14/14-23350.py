num = 39*121**319 + 46*11**913 - 15*1331**15 - 1993

cnt = 0
while num:
    if 104 >= num % 121 >= 64:
        cnt +=1
    num //= 121

print(cnt)