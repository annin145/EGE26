with open(r'.\file\24_1205-perebor.txt') as file:
    data = file.readline()

for i in 'GWP':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))