with open(r'.\file\24_864.txt') as file:
    data = file.readline()

for i in 'EYUIOA':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))