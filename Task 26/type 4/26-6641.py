with open(r'..\files\26_6641.txt') as file:
    N, M = map(int,file.readline().split())
    costs = []
    for line in file:
        price,info = line.split()
        costs.append([int(price), 0 if info == 'W' else 1])

costs = sorted(costs, key=lambda x: (x[0], -x[1]))
cnt_S = 0
buy = []
summ = 0
for cost in costs:
    if summ + cost[0] <= M:
        summ += cost[0]
        buy.append(cost)
        cnt_S += cost[1]

pos_buy = len(buy)
for cost1 in buy[::-1]:
    if cost1[1] == 0:
        for cost2 in costs[pos_buy:]:
            pos_buy += 1
            if cost2[1] == 1:
                if summ - cost1[0] + cost2[0] <= M:
                    buy.remove(cost1)
                    buy.append(cost2)
                    cnt_S += 1
                    summ += -cost1[0] + cost2[0]
                    break

print(cnt_S, M - summ)
