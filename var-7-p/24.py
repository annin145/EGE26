with open(r'.\24_19254.txt') as file:
    data = file.readline()

data = data.replace('FSRQ', 'Fsrq fsrQ')
data = data.split()
ans = 0
for i in range(len(data)-81):
    line = ''.join(data[i:i+81]).replace('srqfsr', 'SR')
    cnt = 0
    for j in data[i+81][4:]:
        cnt +=1
    ans = max(ans,cnt)

print(ans)