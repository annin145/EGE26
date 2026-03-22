with open(r'.\file\24_8510.txt') as file:
    data = file.readline()

for i in data:
    if i in 'NO':
        data = data.replace(i,'N')

for i in data:
    if i in 'NN':
        data = data.replace('NN','N N')

data = data.split()

print(len(max(data, key=len)))