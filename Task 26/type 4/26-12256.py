with open(r'../files/26_12256.txt') as file:
    S, N = map(int,file.readline().split())
    weights = [int(i) for i in file]

weights = sorted(weights)
truck = []
for weight in weights:
    if sum(truck) + weight <= S:
        truck.append(weight)

truck.pop()
for weight in weights[::-1]:
    if sum(truck) + weight <= S:
        truck.append(weight)
        break

print(len(truck), truck[-1])