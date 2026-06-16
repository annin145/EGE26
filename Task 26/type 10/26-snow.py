with open(r'..\files\26_23570.txt') as file:
    N, K = map(int, file.readline().split())
    file = file.readlines()
    dachas = [int(i) for i in file[:N]]
    machines = [list(map(int, i.split())) for i in file[N:]]

dachas = sorted(dachas)

machines = sorted(machines, key=lambda x: [x[1], -x[0]])
last_mod = 0
summ = 0

for d in dachas:
    for s in machines.copy():
        if s[0] >= d:
            last_mod = s[0]
            summ += s[1]
            break
        else:
            machines.remove(s)

print(summ, last_mod)

############################################################

with open(r'../files/26_23570.txt') as file:
    N, K = map(int, file.readline().split())
    ter = [int(file.readline()) for i in range(N)]
    mod = [list(map(int, file.readline().split())) for j in range(K)]

ter = sorted(ter)
mod = sorted(mod, key=lambda x: (x[1], -x[0]))
new_mod = {}

for m in mod:
    if m[0] not in new_mod:
        new_mod[m[0]] = m[1]
    else:
        new_mod[m[0]] = min(new_mod[m[0]], m[1])

price_last_mod = 0
summ = 0

for t in ter:
    for m in new_mod:
        if m >= t:
            price_last_mod = m
            summ += new_mod[m]
            break

print(summ, price_last_mod)