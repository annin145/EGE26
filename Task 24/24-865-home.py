with open(r'.\file\24_865 (1).txt') as file:
    data = file.readline()

ans = 0
cnt = 0
for i in data:
    if i not in 'CF':
        cnt += 1
    else:
        ans = max(ans,cnt)
        cnt = 0
ans = max(ans,cnt)
print(ans)