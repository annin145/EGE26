with open(r'..\file\24_23206.txt') as file:
    data = file.readline()

for i in '02468':
    data = data.replace(i, ' 0')

data = data.split()
ans = 0
for line in data:
    if line.count('S') == 35:
        ans = max(ans, len(line))
    elif line.count('S') > 35:
        cnt_S = line.count('S')
        while cnt_S > 35:
            if line[-1] == 'S':
                cnt_S -= 1
            line = line[:-1]
        ans = max(ans, len(line))
print(ans)


####################################################

with open(r'..\file\24_23206.txt') as file:
    data = file.readline()

for i in '02468':
    data = data.replace(i, ' 0')

data = data.split()
ans = 0
for line in data:
    if line.count('S') == 35:
        ans = max(ans, len(line))
    elif line.count('S') > 35:
        cnt_S = 0
        for i in range(len(line)):
            if line[i] == 'S':
                cnt_S += 1
                if cnt_S == 36:
                    ans = max(ans, i)
                    break
print(ans)


####################################################

with open(r'..\file\24_23206.txt') as file:
    data = file.readline()

for i in '02468':
    data = data.replace(i, ' 0')

data = data.split()
ans = 0
for line in data:
    if line.count('S') == 35:
        ans = max(ans, len(line))
    elif line.count('S') > 35:
        pos_S = [i for i in range(len(line)) if line[i] == 'S']
        ans = max(ans, len(line[:pos_S[35]]))
print(ans)