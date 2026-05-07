with open(r'..\file\24_7600.txt') as file:
    data = file.readline()

ans = 0
cnt = 1
for i in range(len(data)-1):
    if data[i] not in 'QRS' or data[i+1] not in 'QRS':
        cnt += 1
    else:
        cnt = 1
    ans = max(ans,cnt)

print(ans)