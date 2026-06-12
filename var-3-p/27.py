from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\27_A_29077.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'N' and data[2:] == 'I' and data[1] == '9':
            stars.append(dots[-1])

eps = 1.2
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d) < eps:
                cluster.append(d)
                dots.remove(d)
    clusters.append(cluster)

centers = [center(cluster) for cluster in clusters]

distant1 = dist(centers[0], *stars)
distant2 = dist(centers[1], *stars)
print(distant2*10_000,distant1*10_000)

with open(r'.\27_B_29077.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] in '89':
            stars.append(dots[-1])

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
cnt1 = 0
cnt2 = 0
cnt3 = 0
for s in stars:
    for y in clusters[0]:
        if s == y:
            cnt1 += 1

for s in stars:
    for y in clusters[1]:
        if s == y:
            cnt2 += 1
for s in stars:
    for y in clusters[2]:
        if s == y:
            cnt3 += 1

print(cnt1,cnt2,cnt3)

