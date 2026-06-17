with open(r'.\9-3.txt') as file:
    data = [list(map(int,i.split())) for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    if amount == [1,1,1,1,1]:
        if line == sorted(line):
            if (max(line)+min(line)) <= (sum(line) - max(line) - min(line)):
                cnt += 1

print(cnt)
