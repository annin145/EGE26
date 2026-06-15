with open(r'../files/26_15_23259.txt') as file:
    N, M = map(int,file.readline().split())
    for line in file:
        weights = [int(i) for i in line[:M]]
        gruzs = [int(i) for i in line[M:]]

weights = sorted(weights)
gruzs = sorted(gruzs)
cnt = 0
block = []
for weight in weights:
    for gruz in gruzs:
        if weight <= gruz:
            block.append(gruz)


print(len(block))

