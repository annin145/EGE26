with open(r'..\file\24_2942.txt') as file:
    data = file.readline()

cnt = 0
for i in range(len(data)-1):
    if data[i] + data[i+1] == 'AB':
        cnt += 1

for i in range(len(data)-1):
    if data[i] + data[i+1] == 'AC':
        cnt += 1

print(cnt)