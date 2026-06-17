with open(r'.\9-2.txt') as file:
    data = [list(map(int,i.split())) for i in file]

cnt = 0
for line in data:
    if max(line) < (sum(line) - max(line)):
        if (max(line)+min(line)) != (sum(line)-max(line)-min(line)):
            cnt += 1

print(cnt)