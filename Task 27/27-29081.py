from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]

with open(r'.\files\27_A_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x,y,data = i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[2:] == 'VII':
            stars.append(dots[-1])

cluster1 = [d for d in dots if d[1] > 8]
cluster2 = [d for d in dots if d[1] < 8]

stars1 = [d for d in stars if d[1] > 8]
stars2 = [d for d in stars if d[1] < 8]

center1 = center(cluster1)
center2 = center(cluster2)

re = []
for i in stars1:
    re.append(dist(i,center1))
for i in stars2:
    re.append(dist(i,center2))

print(min(re)*10_000)

print(max(re)*10_000)

#######################################

cluster_1 = [[d for d in dots if d[1] > 8],
             [d for d in stars if d[1] > 8]]

cluster_2 = [[d for d in dots if d[1] < 8],
             [d for d in stars if d[1] < 8]]

clusters = [cluster_1, cluster_2]
A = [dist(center(cl[0]), s) for cl in clusters for s in cl[1]]
print(min(A) * 10_000, max(A) * 10_000)

