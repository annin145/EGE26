from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]

with open(r'.\files\27_B_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0] == 'Z' and data[2:] == 'I':
            stars.append(list(map(float,[x,y])))

cluster1 = [dot for dot in dots if dot[1] < 15]
cluster2 = [dot for dot in dots if 15 < dot[1] < 23]
cluster3 = [dot for dot in dots if 23 < dot[1]]

clusters = [cluster1,cluster2,cluster3]
# cluster_s = []
#
# # for i in clusters:
# #     for s in stars:
# #         if i in s:
# #             cluster_s.append(s)
#
# print(cluster_s)

cluster01 = []
cluster02 = []
cluster03 = []
for s in stars:
    if s in cluster1:
        cluster01.append(s)
    if s in cluster2:
        cluster02.append(s)
    if s in cluster3:
        cluster03.append(s)

print(cluster01)
print()
print(cluster02)
print()
print(cluster03)
print()

center1 = center(cluster1)
center2 = center(cluster2)

B2 = dist(center1,center2)

B1 = []
for s in cluster01:
    for y in cluster01:
        if s != y:
            B1.append(dist(s,y))

for s in cluster03:
    for y in cluster03:
        if s != y:
            B1.append(dist(s,y))

print(min(B1)*10_000)
print(B2*10_000)

# второй вариант решения пункта B

#from itertools import combinations
# from math import dist
#
# def center(cluster):
#     res = []
#     for dot in cluster:
#         sum_dist = sum(dist(dot, d) for d in cluster)
#         res.append([sum_dist, dot])
#     return min(res)[1]
#
# with open(r'.\files\27_B_28766.txt') as file:
#     dots = []
#     stars = []
#     for i in file:
#         x, y, data = i.replace(',', '.').split()
#         dots.append(list(map(float, [x, y])))
#         if data[0] == 'Z' and data[2:] == 'I':
#             stars.append(list(map(float, [x, y])))
#
# cluster_1 = [
#     [d for d in dots if 23 < d[1]],
#     [d for d in stars if 23 < d[1]]
# ]
#
# cluster_2 = [
#     [d for d in dots if 16 < d[1] < 23],
#     [d for d in stars if 16 < d[1] < 23]
# ]
#
# cluster_3 = [
#     [d for d in dots if d[1] < 16],
#     [d for d in stars if d[1] < 16]
# ]
#
# clusters = [cluster_1, cluster_2, cluster_3]
#
# dists = []
# for cluster in clusters:
#     dists += [dist(d1, d2) for d1, d2 in combinations(cluster[1], 2)]
# B1 = min(dists)
#
# max_cluster = center(max(clusters, key=lambda x: len(x[1]))[0])
# min_cluster = center(min(clusters, key=lambda x: len(x[1]))[0])
# B2 = dist(max_cluster, min_cluster)
#
# print(B1 * 10_000, B2 * 10_000)
