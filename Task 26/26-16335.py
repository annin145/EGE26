
with open(r'.\files\26_16335.txt') as file:
    N = int(file.readline())
    cakes = [int(i) for i in file]

cakes = sorted(set(cakes))[::-1]

last_cake = cakes[0]
cnt = 1
for cake in cakes:
    if last_cake - cake >= 4:
        last_cake = cake
        cnt += 1

print(cnt,last_cake)