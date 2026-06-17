with open(r'.\9-1.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1,1,1,1,3]:
        pov = [i for i in line if line.count(i) != 1]
        not_pov = [i for i in line if line.count(i) == 1]
        if sum(not_pov) / len(not_pov) > pov[0]:
            print(pos)