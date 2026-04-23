from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]

with open(r'.\files\27_A_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0] == 'Y' and data[2:] == 'III':
            stars.append(list(map(float,[x,y])))

cluster1 = [dot for dot in dots if dot[1] > 8]
cluster2 = [dot for dot in dots if dot[1] < 8]

center1 = center(cluster1)
center2 = center(cluster2)
# clusters = [cluster1, cluster2]
# print(min(clusters,key=len))
print(len(cluster1), len(cluster2))

# dists = dist(cluster1, stars)
print(center1)
print(stars)

dists = [dist(center1,s) for s in stars]

print()
print(min(dists)*10_000)
print(max(dists)*10_000)