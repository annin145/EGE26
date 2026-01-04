with open(r'.\file\24_1874.txt') as file:
    data = file.readline()

data = data.replace('QW', 'Q W')
data = data.split()

print(len(max(data, key=len)))