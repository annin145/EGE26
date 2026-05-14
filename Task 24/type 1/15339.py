with open(r'..\file\24_15339.txt') as file:
    data = file.readline()

ans = 0
cnt = 1
for i in range(len(data)-1):
    if (data[i] in 'ABC' and data[i+1] in '6789') or (data[i] in '6789' and data[i+1] in 'ABC'):
        cnt += 1
    else:
        cnt = 1
    ans = max(ans,cnt)

print(ans)

