with open(r'..\file\24_6757.txt') as file:
    data = file.readline()

for i in 'CF':
    for j in 'CF':
        for z in 'E':
            data = data.replace(i+j+z, '*')

for i in 'CDFE':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data,key=len)))
