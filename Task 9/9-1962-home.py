with open(r'.\files\1962.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    for i in range(len(line)+1):
        a,b,c = data[i:i+3]
        if a+b > c and b+c > a and c+a > b:
            cnt += 1
print(cnt)

