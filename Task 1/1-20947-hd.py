from itertools import *

graph = 'ав вд де еи иг гб ба бв гж жд жи'.split()
matrix = '267 157 468 356 248 134 12 35'.split()

print(*(range(1,9)))
for i in permutations('абвгдеиж'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)