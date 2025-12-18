from itertools import permutations

graph = 'ad dc cf fg ge ea ah hg hb bc bd'.split()
matrix = '346 348 12 127 678 15 458 257'.split()

print(*range(1,9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)