from itertools import permutations

graph = 'af fc cd db be eg ga fg bc'.split()
matrix = '24 134 267 125 47 37 356'.split()

print(*range(1,9))
for i in permutations('abcdefg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)