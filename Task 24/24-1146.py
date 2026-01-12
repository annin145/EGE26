with open(r'.\file\24_1146.txt') as file:
    data = file.readline()

ans = 10**18
cnt = 0
for i in data:
    if i == 'D':
        cnt +=1
    elif cnt != 0:
        ans = min(ans,cnt)
        cnt = 0

if cnt != 0: ans = min(ans,cnt)
print(ans)