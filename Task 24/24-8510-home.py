with open(r'.\file\24_8510.txt') as file:
    data = file.readline()

for i in 'PO':
    data = data.replace(i,'N')

while 'NN' in data:
    data = data.replace('NN','N N')

data = data.split()

print(len(max(data, key=len)))