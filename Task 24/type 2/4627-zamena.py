with open(r'..\file\24_4627.txt') as file:
    data = file.readline()

data = data.replace('NPO', '*')
data = data.replace('PNO', '*')

data = data.replace('N', ' ')
data = data.replace('P', ' ')
data = data.replace('O', ' ')

data = data.split()

print(len(max(data, key=len)))