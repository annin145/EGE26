from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]

with open(r'.\27_A_29075 (1).txt') as file:
    dots = []
    stars = []
    for i in file:
        x,y,data = i.replace(',', '.').split()
        dots.append(list(map(float, [x,y])))
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
print(centers[1][0]*10_000)
print(centers[0][1]*10_000)


with open(r'.\27_B_29075 (1).txt') as file:
    dots = []
    stars = []
    for i in file:
        x,y,data = i.replace(',', '.').split()
        dots.append(list(map(float, [x,y])))
        if data[0] == 'J':
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
            cnt2 += [s]
r = [dist(t,p) for p in cnt1 for t in cnt2]+[dist(t,p) for p in cnt2 for t in cnt3]+\
    [dist(t,p) for p in cnt1 for t in cnt3]
B1 = int(min(r)*10_000)
B2 = int(max(r)*10_000)

print(B1)
print(B2)

