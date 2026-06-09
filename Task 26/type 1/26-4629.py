with open(r'..\files\26_4629.txt') as file:
    N = int(file.readline())
    costs = [int(i) for i in file]

costs = sorted(costs, reverse=True)
cost = sorted(costs)
price1 = sum(costs) - sum(cost[:N //4]) //2
price2 = sum(costs) - sum(costs[:N // 4]) // 2

print(price2,price1)


