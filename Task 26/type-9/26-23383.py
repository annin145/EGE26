with open(r'..\files\26_23383.txt') as file:
    N = int(file.readline())
    sports = [list(map(int,i.split())) for i in file]

sports = sorted(sports, key=lambda x: (x[1], x[0]))
cnt = 1
point = []
for sports1,sports2 in zip(sports,sports[1:]):
    if sports1 == sports2:
        continue
    if sports2[0] - sports1[0] == 1 and sports1[1] == sports2[1]:
        cnt += 1
        point.append([cnt,sports2[1]])
    else:
        cnt = 1

print(*max(point, key=lambda x: (x[0], -x[1])))

