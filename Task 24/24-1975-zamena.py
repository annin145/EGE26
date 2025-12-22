with open(r'.\file\24_1975-perebor.txt') as file:
    data = file.readline()

while 'PP' in data:
    data = data.replace('PP', 'P P')

data = data.split()
print(len(max(data, key=len)))