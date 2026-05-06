with open(r'..\file\24_7624.txt') as file:
    data = file.readline()

data = data.replace('XX', 'X X')
data = data.replace('YY', 'Y Y')
data = data.replace('ZZ', 'Z Z')
data = data.replace('XY', 'X Y')
data = data.replace('XZ', 'X Z')
data = data.replace('ZX', 'Z X')
data = data.replace('YX', 'Y X')
data = data.replace('ZY', 'Z Y')
data = data.replace('YZ', 'Y Z')

data = data.split()
# print(data)
print(len(max(data,key=len)))
