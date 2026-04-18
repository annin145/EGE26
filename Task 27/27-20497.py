from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist,dot])
    return max(res)[1]

with open(r'./files/27.19.A_20497.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]

# eps = 1
# clusters = []
# while dots:
#     cluster = [dots.pop()]
#     for dot in cluster:
#         for d in dots.copy():
#             if dist(dot,d) < eps:
#                 cluster.append(d)
#                 dots.remove(d)
#     clusters.append(cluster)
#
# centers = [center(cluster) for cluster in clusters]
#
# print([len(cluster) for cluster in clusters])

cluster1 = [dot for dot in dots if dot[1] > 0]
cluster2 = [dot for dot in dots if dot[1] < 0 and dot[0] < 0]
cluster3 = [dot for dot in dots if dot[1] < 0 and dot[0] > 0]
