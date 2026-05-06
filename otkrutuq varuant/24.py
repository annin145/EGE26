with open(r'.\24_29354.txt') as file:
    data = file.readline()

ans = []
cnt = 0
for i in range(len(data)-1):
    if data[i] + data[i+1] != 'BC':
        cnt += 1
        if cnt == 190:
            ans.append(len(data))
            data.split()

print(ans)
