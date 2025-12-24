from itertools import permutations

graph = 'ae ed db bg gc ca cf gf fe'.split()
matrix = '26 147 456 237 37 13 245'.split()

print(*(range(1,9)))
for i in permutations('abcdefg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

#60