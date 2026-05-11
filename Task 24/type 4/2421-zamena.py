from string import printable
with open(r'..\file\24_21421.txt') as file:
    data = file.readline().lower()

for i in printable[12:]:
    data = data.replace(i, ' ')

data = data.split()

ans = 0
for line in data:
    line = line.rstrip('13579b').lstrip('0')
    ans = max(ans, len(line))

print(ans)