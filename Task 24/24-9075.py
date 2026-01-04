with open(r'./file/24_9075.txt') as file:
    data = file.readline()

cnt = 1
ans = 0
for i in range(1, len(data)-1):
    if int(data[i]) % 2 != int(data[i + 1]) % 2:
            cnt +=1
    else:
        ans = max(ans, cnt)
        cnt = 1

ans = max(ans,cnt)
print(ans)
