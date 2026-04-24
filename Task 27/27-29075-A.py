from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_A_29075.txt') as file:
    dots = []
    stars = []
    for i in file:
        x,y,data = i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[2:] == 'III':
            stars.append(list(map(float,[x,y])))

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 30:
        clusters.append(cluster)

centers = [center(cluster) for cluster in clusters]
print([len(cluster) for cluster in clusters])

cnt1 = 0
cnt2 = 0
for s in stars:
    for y in clusters[0]:
        if s == y:
            cnt1 += 1

for s in stars:
    for y in clusters[1]:
        if s == y:
            cnt2 += 1

print(cnt1,cnt2)
print()
print(centers[1][0]*10_000)
print(centers[0][1]*10_000)
