from itertools import *

graph = 'af fe ec eb bc bd da ac'.split()
matrix = '36 456 145 236 23 124'.split()

print(*(range(1,9)))
for i in permutations('abcdef'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)