with open(r'..\files\26_17881.txt') as file:
    N = int(file.readline())
    res_0 = []
    res_3 = []
    for line in file:
        ID, *exs = map(int,line.split())
        if exs.count(2) == 0:
            res_0.append([sum(exs) / 4, ID])
        elif exs.count(2) == 3:
            res_3.append([sum(exs) / 4, ID])

res_0 = sorted(res_0, key=lambda x: (-x[0],x[1]))
res_3 = sorted(res_3, key=lambda x: (-x[0],x[1]))

print(res_0[:N//4][-1][1], res_3[0][1])