with open(r'..\file\24_7624.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data)-1):
    if data[i] not in 'XYZ' and data[i+1] not in 'XYZ':
        cnt = 1
        for j in range(i+2,len(data)-1,2):
            if data[i] not in 'XYZ' and data[i+1] not in 'XYZ':
                cnt += 1
            else:
                break
        ans = max(ans,cnt)

print(ans)
