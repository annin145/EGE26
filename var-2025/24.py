with open(r'.\24_23281.txt') as file:
    data = file.readline()
ans = []
data = data.split('Y')
for i in range(len(data)-80):
    line = 'Y'.join(data[i:i+81])
    if line.count('2025') >= 90:
        ans.append(len(line))

print(max(ans))