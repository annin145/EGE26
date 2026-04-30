with open(r'..\file\24_1975-perebor.txt') as file:
    data = file.readline()

# data = '***PPP*******PP**'
ans = 0
cnt = 1
for i in range(len(data)-1):
    if data[i] + data[i+1] != 'PP':
        cnt += 1
    else:
        cnt = 1
    ans = max(ans,cnt)


print(ans)
