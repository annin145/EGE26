with open(r'..\files\26_23283.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    guests = [list(map(int,i.split())) for i in file]
guests = sorted(guests)
places = [0] * K
cnt = 0
pos = 0
for guest in guests:
    for i in range(K):
        if places[i] < guest[0]:
            places[i] = guest[1]
            cnt = i + 1
            pos += 1
            break
print(pos,cnt)
