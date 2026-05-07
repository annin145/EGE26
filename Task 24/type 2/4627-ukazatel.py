with open(r'..\file\24_4627.txt') as file:
    data = file.readline()

ans = cnt = i = 0

while i < len(data) - 2:
    if data[i:i+3] in 'PNO NPO':
        cnt += 1
        i += 3
    else:
        cnt = 0
        i += 1
    ans = max(ans,cnt)

print(ans)