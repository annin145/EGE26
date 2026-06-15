with open(r'..\files\26_17643.txt') as file:
    N = int(file.readline())
    data = [list(map(int,i.split())) for i in file]

middle = sum(i[1] for i in data) / N
products = {}
for ID, price,status in data:
    if price > middle:
        if ID not in products:
            if status: products[ID] = [0,price,1]
            else: products[ID] = [1,price,0]
        else:
            products[ID][2] += status
            products[ID][0] += (not status)

keys= sorted(products, key=lambda x: (products[x][0], products[x][1], -products[x][2]))

print(products[keys[-1]][0] * products[keys[-1]][1], products[keys[-1]][-1])
