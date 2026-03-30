with open(r'.\files\7030.txt') as file:
    data = [list(map(int,i.split())) for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [2,2,2]:
        if max(line)**2 == (sum(line)- max(line) - min(line))**2 + min(line)**2:
            cnt += 1

print(cnt)