with open(r'..\files\26_4684.txt') as file:
    N = int(file.readline())
    costs = [int(i) for i in file]

cost = sorted(costs)
price2 = sum(cost) - sum(cost[:N//6])//2
price1  = sum(cost) - sum(cost[::-1][5::6])//2
#
print(price1,price2)

price_1 = sum(cost) - sum(cost[:N//6+1])//2

print(price_1)
# print(cost)