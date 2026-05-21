from itertools import permutations

graph = 'ям мк кт тл лв ву уя ок от ле ев'.split()
matrix = '25 159 78 67 126 457 346 39 28'.split()

print(*range(1,10))
for i in permutations('ямкотлеву'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)