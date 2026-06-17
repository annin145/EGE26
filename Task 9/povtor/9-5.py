with open(r'.\9-5.txt') as file:
    data = [list(map(int,i.split())) for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    if amount == [1,1,1,1,1]:
        if ((max(line)+min(line))*2) == (sum(line)- max(line)-min(line)):
            cnt += 1

print(cnt)