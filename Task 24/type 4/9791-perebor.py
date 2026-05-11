from string import printable
with open(r'..\file\24_9791.txt') as file:
    data = file.readline().lower()

cnt = 0
ans = 0
for i in data:
    if i in printable[:16]:
        cnt += 1
    else:
        cnt = 0
    ans = max(ans,cnt)

print(ans)