from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27A_27138.txt') as file:
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

centers = [center(cluster) for cluster in clusters]


print((centers[0][0] - centers[1][0])*10_000)
print((centers[0][1] - centers[1][1])*10_000)

with open(r'.\files\27B_27138.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]

eps = 20
clusters = []

while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) == 1:
        clusters.append(cluster)

# centers = [center(cluster) for cluster in clusters]
# print(centers)
# cl3 = clusters[2]
# print(cl3)
# # print([len(cluster) for cluster in clusters])
# print(max(cl3)[0])

print(clusters)
print((clusters[0]+clusters[1])*10_000)

