from itertools import permutations

graph = 'af fe ed dc cb bg ga gf ge gd gc'.split()
matrix = '345 467 14 123567 147 24 245'.split()

print(*range(1,9))
for i in permutations('abcdefg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)