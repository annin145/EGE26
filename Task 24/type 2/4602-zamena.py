with open(r'..\file\24_4602.txt') as file:
    data = file.readline()

for i in 'BCD':
    for j in 'AO':
        data = data.replace(i+j, '*')


for i in 'ABCDO':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))