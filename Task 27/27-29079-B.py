with open(r'.\files\27_B_29079.txt') as file:
    dots = []
    stars = []
    for i in file:
        x,y,data = i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0] == 'J' and data[2:] == 'V':
            stars.append(dots[-1])

stars1 = [s for s in stars if 22 < s[1]]
stars2 = [s for s in stars if 16 < s[1] < 22]
stars3 = [s for s in stars if 16 > s[1]]

cluster1 = [s for s in dots if 22 < s[1]]
cluster2 = [s for s in dots if 16 < s[1] < 22]
cluster3 = [s for s in dots if 16 > s[1]]

clusters = [cluster1,cluster2,cluster3]

print([len(cluster) for cluster in clusters])

B1 = max(stars3)
B1 = B1[0]

B2 = []
for i in stars1:
    B2.append(i[1])

print(B1*10_000)
print(max(B2)*10_000)