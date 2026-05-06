from itertools import *

graph = 'аб бв вг ге ек кд дб вд ве ед'.split()
matrix = '27 1567 67 5 246 2357 1236'.split()

print(*range(1,9))
for i in permutations('абвгдек'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)