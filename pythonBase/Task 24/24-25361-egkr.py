with open('24_25361.txt') as file:
    data = file.readline()

for i in '02468':
    data = data.replace(i, ' 0')
data = data.split()

ans = []
for i in data:
    if i[0] == '0':
        if i.count('F') == 76:
            ans.append(len(i))
        elif i.count('F') > 76:
            while i.count('F') > 76:
                pos_F = i.rfind('F')
                i = i[:pos_F]
            ans.append(len(i))
print(max(ans))
