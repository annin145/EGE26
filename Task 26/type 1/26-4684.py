with open(r'..\files\26_4684.txt') as file:
    N = int(file.readline())
    costs = [int(i) for i in file]

cost = sorted(costs)
price2 = sum(costs[:-(N//6)]) + sum(costs[-(N//6):])//2
price1  = sum(costs) - sum(costs[::-1][5::6])//2

print(price1,price2)

