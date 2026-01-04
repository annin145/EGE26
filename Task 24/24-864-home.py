with open(r'.\file\24_864.txt') as file:
    data = file.readline()

ans = 0
cnt = 0
for i in data:
    if i not in 'EYUIOA':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

ans = max(ans, cnt)
print(ans)