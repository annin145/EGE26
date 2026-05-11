from string import printable
with open(r'..\file\24_9791.txt') as file:
    data = file.readline().lower()

for i in printable[16:]:
    data = data.replace(i, ' ')
data = data.split()

ans = 0
for line in data:
    line = line.lstrip('0')
    ans = max(ans, len(line))
print(ans)