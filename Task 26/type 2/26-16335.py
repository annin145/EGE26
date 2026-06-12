with open(r'..\files\26_16335 (1).txt') as file:
    N = int(file.readline())
    cakes = [int(i) for i in file]

cakes = sorted(cakes,reverse=True)
last_cake = cakes[0]
cnt = 1
for cake in cakes:
    if last_cake - cake >= 4:
        cnt +=1
        last_cake = cake

print(cnt, last_cake)