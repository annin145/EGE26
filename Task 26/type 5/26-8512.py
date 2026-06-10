with open(r'..\files\26_8512.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    guests = [list(map(int,i.split())) for i in file]

guests = sorted(guests)
cells = [0] * K
cnt = 0
last_cell = 0
for guest in guests:
    for i in range(K):
        if cells[i] < guest[0]:
            cells[i] = guest[1]
            last_cell = i+1
            cnt +=1
            break

print(cnt,last_cell)