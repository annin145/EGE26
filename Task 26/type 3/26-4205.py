with open(r'..\files\26_4205.txt') as file:
    N = int(file.readline())
    places = [list(map(int,i.split())) for i in file]

places = sorted(places)
pl = []
for place1,place2 in zip(places, places[1:]):
    if place1[0] == place2[0]:
        if place2[1] - place1[1] == 14:
            pl.append([place1[0], place1[1]+ 1])

print(max(pl))

