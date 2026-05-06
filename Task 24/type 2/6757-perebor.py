with open(r'..\file\24_6757.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data)-2):
    if data[i:i+2] in 'CF' and data[i+2] == 'E':
        cnt = 1
        for j in range(i+3,len(data)-2,3):
            if data[i:i+2] in 'CF' and data[i+2] == 'E':
                cnt += 1
            else:
                break
        ans = max(ans,cnt)

print(ans)