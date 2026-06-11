with open(r'..\files\26_17687.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices)
price1 = sum(prices) - sum(prices[-(N//9):])
price2 = sum(prices) - sum(prices[::-1][8::9])

print(price1,price2)