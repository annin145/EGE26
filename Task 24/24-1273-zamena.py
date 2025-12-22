with open(r'.\file\24_1273-perebor.txt') as file:
    data = file.readline()

data = data.replace('XYZ', 'XY YZ')
data = data.split()
print(len(max(data,key=len)))