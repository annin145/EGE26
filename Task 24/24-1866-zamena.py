with open(r'.\file\24_1866-perebor.txt') as file:
    data = file.readline()

data = data.replace('ad', 'a d')
data = data.replace('da', 'd a')
data = data.split()
print(len(max(data,key=len)))