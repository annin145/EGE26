with open(r'.\files\19241.txt') as file:
    data = [list(map(int,i.split())) for i in file]

ans = []
for pos, line in enumerate(data,start=1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1,3,3]:
        pov = [i for i in set(line) if line.count(i) != 1]
        not_pov = [i for i in set(line) if line.count(i) == 1]
        if sum(pov)/len(pov) < not_pov[0]:
            print(pos)