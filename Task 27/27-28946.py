from math import dist
#
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d)for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
#
# with open(r'.\files\27_A_28946.txt') as file:
#     dots = [list(map(float, i.replace(',', '.').split())) for i in file]
#
# eps = 1
# clusters = []
#
# while dots:
#     cluster = [dots.pop()]
#     for dot in cluster:
#         for d in dots.copy():
#             if dist(dot,d) < eps:
#                 cluster.append(d)
#                 dots.remove(d)
#     if len(cluster) > 30:
#         clusters.append(cluster)
#
# centers = [center(cluster) for cluster in clusters]
# print([len(cluster) for cluster in clusters])
#
# center2 = center(clusters[1])
# center1 = center(clusters[0])
# onex = center1[0]
# twoX = center2[0]
#
# print(centers)
# print(center2)
# cnt = 0
# for i in clusters[1]:
#     if i[1] < center2[1]:
#         cnt += 1
# print(cnt) # A1
#
# print(abs(onex-twoX)*10_000)

print()
#33333333333333333333333333333333333333333333333333333
print()

with open(r'.\files\27_B_28946.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 2
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
print([len(cluster) for cluster in clusters])
print(centers)

cnt = 0
m_center = centers[1]
for i in clusters[1]:
    if dist(i,m_center) < 0.9:
        cnt += 1

print(cnt)
print(m_center)
print(clusters[1])

