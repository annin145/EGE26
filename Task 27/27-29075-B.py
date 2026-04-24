from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_B_29075.txt') as file:
    dots = []
    stars = []
    for i in file:
        x,y,data = i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
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
            cnt2 += [s]

# r1 = [dist(p,t) for p in cnt1 for t in cnt2]
# r2 = [dist(p,g) for p in cnt1 for g in cnt3]
# r3 = [dist(t,g) for t in cnt2 for g in cnt3]
#
# print(max(r1))
# print(max(r2))
# print(max(r3))
r = [dist(t,p) for p in cnt1 for t in cnt2]+[dist(t,p) for p in cnt2 for t in cnt3]+\
    [dist(t,p) for p in cnt1 for t in cnt3]
B1 = int(min(r)*10_000)
B2 = int(max(r)*10_000)

print(B1)
print(B2)