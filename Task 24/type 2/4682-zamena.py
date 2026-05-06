with open(r'..\file\24_4682.txt') as file:
    data = file.readline()

for i in 'BCD':
    for j in 'AE':
        data = data.replace(i+j,'*')

for i in 'ABCDE':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data,key=len)))