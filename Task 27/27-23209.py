from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]

with open(r'.\files\27_A_23209.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]

clusterA1 = [dot for dot in dots if dot[1] < 10]
clusterA2 = [dot for dot in dots if dot[1] > 10]

centerA1 = center(clusterA1)
centerA2 = center(clusterA2)

print(max(centerA1[0], centerA2[0]) * 10_000)
print(max(centerA1[1], centerA2[1]) * 10_000)

with open(r'.\files\27_B_23209.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]

clusterB1 = [d for d in dots if 0 < d[1] < 10]
clusterB2 = [d for d in dots if 10 < d[1] < 21]
clusterB3 = [d for d in dots if 21 < d[1] < 26]

centerB1 = center(clusterB1)
centerB2 = center(clusterB2)
centerB3 = center(clusterB3)

cl1 = len(clusterB1)
cl2 = len(clusterB2)
cl3 = len(clusterB3)

print(cl1,cl2,cl3)
print(max(cl1,cl2,cl3), str(min(cl1,cl2,cl3)))
print('//////////////////////////////////////////////////')
print((centerB1[0] - centerB3[0])*10_000)
print((centerB1[1] - centerB3[1])*10_000)


