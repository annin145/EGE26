
with open(r'.\file\24_17535.txt') as file:
    data = file.readline()

data = data.replace('CD','C D').split()

len_max = 0
for i in range(len(data)-160):
    s = ''.join(data[i:i+161])
    len_max = max(len_max, len(s))

print(len_max)