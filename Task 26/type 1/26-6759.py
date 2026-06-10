with open(r'..\files\26_6759.txt') as file:
    N = int(file.readline())
    costs = [int(i) for i in file]

costs = sorted(costs)
price1 = sum(costs[::-1][N//3:])
price2 = sum(costs) - sum(costs[::-1][2::3])

print(price1, price2)