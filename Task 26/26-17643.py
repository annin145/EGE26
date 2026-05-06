with open(r'.\files\26_17643.txt') as file:
    N = int(file.readline())
    goods = [list(map(int, i.split())) for i in file]

avg = sum(good[1] for good in goods) / N

epx = {}
for good in [good for good in goods if good[1] > avg]:
    if good[0] not in epx:
        epx[good[0]] = [not good[2], good[1], good[2]]
    else:
        epx[good[0]][0] += not good[2]
        epx[good[0]][2] += good[2]

epx = sorted(epx.values(), key=lambda  x: (-x[0],-x[1], x[2]))[0]

print(epx[0]* epx[1], epx[2])