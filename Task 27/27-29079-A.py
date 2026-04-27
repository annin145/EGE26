from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]

with open(r'.\files\27_A_29079.txt') as file:
    dots = []
    stars = []
    for i in file:
        x,y,data = i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0] == 'N' and data[2:] == 'IV':
            stars.append(dots[-1])

cluster1 = [d for d in dots if d[1] > 8]
cluster2 = [d for d in dots if d[1] < 8]

stars1 = [d for d in stars if d[1] > 8]
stars2 = [d for d in stars if d[1] < 8]

center1 = center(cluster1)
center2 = center(cluster2)

dists = []
for s in stars1:
    dists.append(dist(s,center2))

for s in stars2:
    dists.append(dist(s,center1))

A1 = min(dists)
A2 = max(dists)

print(A1*10_000)
print(A2*10_000)