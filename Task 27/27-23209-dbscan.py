from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]

with open(r'.\files\27_A_23209.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d) < eps:
                cluster.append(d)
                dots.remove(d)
    clusters.append(cluster)

print([len(cluster) for cluster in clusters])

centers = [center(cluster) for cluster in clusters]

print(max(centers, key=lambda x: x[0])[0]*10_000)
print(max(centers, key=lambda x: x[1])[1]*10_000)

with open(r'.\files\27_B_23209.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 1:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])

centers = [[len(cluster), center(cluster)] for cluster in clusters]

max_cl = max(centers)
min_cl = min(centers)

print((max_cl[1][0] - min_cl[1][0])*10_000)
print((max_cl[1][1] - min_cl[1][1])*10_000)

