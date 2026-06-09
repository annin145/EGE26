with open(r'..\files\26_3586.txt') as file:
    N = int(file.readline())
    places = [list(map(int,i.split())) for i in file]

places = sorted(places)
pl = []
for place1,place2 in zip(places,places[1:]):
    if place1[0] == place2[0]:
        pl.append([place2[1] - place1[1]-1, place1[0]])

print(max(pl)[::-1])