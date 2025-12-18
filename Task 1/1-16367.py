from itertools import permutations

graph = 'ac cd df fe eb bg ga ba fc'.split()
matrix = '246 16 57 15 347 127 356'.split()

print(*(range(1,9)))
for i in permutations('abcdefg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)