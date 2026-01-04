from itertools import permutations

graph = 'аб бд де еж жз за ав бв вг гд зе'.split()
matrix = '345 35 128 156 124 478 68 367'.split()

print(*(range(1,9)))
for i in permutations('абвгдежз'):
    if all(str(i.index(x)+ 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

#б г д а в з ж е