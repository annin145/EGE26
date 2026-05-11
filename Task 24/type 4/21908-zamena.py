from string import printable

with open(r'..\file\24_21908.txt') as file:
    data = file.readline().lower()


for i in printable[14:]:
    data = data.replace(i, ' ')

data = data.split()

ans = '0'
for line in data:
    line = line.rstrip('13579bd').lstrip('0')
    if line:
        ans = max(ans, line, key=lambda x: int(x,14))
print(ans)



