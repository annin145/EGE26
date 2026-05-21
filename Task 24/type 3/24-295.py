with open(r'..\file\24-295 (1).txt') as file:
    data = file.readline()

data = data.replace('DE', 'D E').split()

ans = 0
for i in range(len(data)-240):
    line = ''.join(data[i:i+241])
    ans = max(ans,len(line))

print(ans)