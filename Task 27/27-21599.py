from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\27_A_21599.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]

clusterA1 = [dot for dot in dots if dot[1] < -7]
clusterA2 = [dot for dot in dots if -7 < dot[1] < 11/14 * dot[0] - 11]
clusterA3 = [dot for dot in dots if dot[1] > 11/14 * dot[0] - 11]

centerA1 = center(clusterA1)
centerA2 = center(clusterA2)
centerA3 = center(clusterA3)

print((centerA1[0] + centerA2[0] + centerA3[0]) / 3 * 10_000)
print((centerA1[1] + centerA2[1] + centerA3[1]) / 3 * 10_000)

with open(r'.\files\27_B_21599.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]

clusterB1 = [ dot for dot in dots if dot[1] < -5]
clusterB2 = [ dot for dot in dots if -5 < dot[1] < dot[0]]
clusterB3 = [ dot for dot in dots if  (10/7 * dot[0] + 10) > dot[1] > dot[0]]
clusterB4 = [ dot for dot in dots if  (10/7 * dot[0] + 10) < dot[1] and -10 < dot[0]]
clusterB5 = [ dot for dot in dots if  (-2 * dot[0] -26) < dot[1]  and -10 > dot[0]]
clusterB6 = [ dot for dot in dots if  (-2 * dot[0] -26) > dot[1] > -5]

centerB1 = center(clusterB1)
centerB2 = center(clusterB2)
centerB3 = center(clusterB3)
centerB4 = center(clusterB4)
centerB5 = center(clusterB5)
centerB6 = center(clusterB6)
# clusters = [clusterB1,clusterB2,clusterB3,clusterB4,clusterB5,clusterB6]

print()
print((centerB1[0] + centerB2[0] +centerB3[0] +centerB4[0] +centerB5[0] +centerB6[0])/6 * 10_000)
print((centerB1[1] + centerB2[1] +centerB3[1] +centerB4[1] +centerB5[1] +centerB6[1])/6 * 10_000)
