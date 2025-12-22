from itertools import permutations

graph = 'af fc cg ge ed da ab bf be'.split()
matrix = '37 367 125 56 34 247 126'.split()

print(*(range(1,8)))
for i in permutations('abcdefg'):
    if all(str(i.index(x) +1) in matrix[i.index(y)] for x,y in graph):
        print(*i)