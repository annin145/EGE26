from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_B_29076.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0] == 'Y':
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

cnt1 = []
cnt2 = []
cnt3 = []
for s in stars:
    for y in clusters[0]:
        if s == y:
            cnt1 += [s]

for s in stars:
    for y in clusters[1]:
        if s == y:
            cnt2 += [s]

for s in stars:
    for y in clusters[2]:
        if s == y:
            cnt3 += [s]

print(cnt1,cnt2,cnt3)

center1 = centers[0]
center2 = centers[1]
center3 = centers[2]

print(dist(center1,center3)*10_000)

r = [dist(center1,p) for p in cnt1]+[dist(center2,p) for p in cnt2]+\
    [dist(center3,p) for p in cnt3]
B2 = int(max(r)*10000)

print(B2)