with open(r'.\files\23747.txt') as file:
    data = [list(map(int,i.split())) for i in file]

ans = []
for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1,1,1,1,3]:
        not_pov = [i for i in set(line) if line.count(i) == 1]
        pov = [i for i in set(line) if line.count(i) != 1]
        if pov[0] >= sum(not_pov)/len(not_pov):
            ans.append(sum(line))

print(ans[-1])