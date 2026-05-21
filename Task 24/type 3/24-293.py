with open(r'..\file\24-293.txt') as file:
    data = file.readline()

data = data.split('D')
ans = 0
for i in range(len(data)-100):
    line = 'D'.join(data[i:i+101])
    for j in '0123456789':
        if j not in line:
            if 'DS' not in line and 'SD' not in line:
                ans = max(ans, len(line))

print(ans)