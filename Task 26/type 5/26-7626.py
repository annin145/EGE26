with open(r'..\files\26_7626.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    guests = [list(map(int,i.split())) for i in file]

guests = sorted(guests)
cell = [0] * K
cnt = 0
last_cell = 0
for guest in guests:
    for i in range(K):
        if cell[i] < guest[0]:
            cell[i] = guest[1]
            last_cell = i+1
            cnt += 1
            break

print(cnt,last_cell)