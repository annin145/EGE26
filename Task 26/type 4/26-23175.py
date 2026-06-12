with open(r'../files/26_2_23175.txt') as file:
    N, M = map(int, file.readline().split())
    weights = [int(file.readline()) for i in range(N)]
    containers = [int(file.readline()) for i in range(M)]

loaded = []
weights = sorted(weights)
containers = sorted(containers)
last_container = 0
for weight in weights:
    for container in containers:
        if container - weight >= 0:
            loaded.append(weight)
            last_container = container
            containers.remove(container)
            break
loaded = loaded[:-1]
for weight in weights[::-1]:
    if last_container - weight >= 0:
        loaded.append(weight)
        break

print(len(loaded), loaded[-1] - loaded[-2])

















# cnt = 0
# ns = weights[:900]
# ns = sorted(ns)
# ms = weights[900:]
# ms = sorted(ms)
# last_cont = []
# for m in ms:
#     conts = [m] * M
#     for n in ns:
#         for cont in conts:
#             if n <= cont:
#                 cnt += 1
#                 cont = n
#                 last_cont.append(n)
#                 break
# last_cont = sorted(last_cont,reverse=True)
# print(cnt,last_cont[-1] - last_cont[-2])


