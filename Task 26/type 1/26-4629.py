with open(r'..\files\26_4629.txt') as file:
    N = int(file.readline())
    costs = [int(i) for i in file]

costs = sorted(costs, reverse=True)
price1 =sum(costs) - sum(costs[3::4]) //2


