with open(r'.\file\24_865 (1).txt') as file:
    data = file.readline()

for i in 'CF':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data,key=len)))