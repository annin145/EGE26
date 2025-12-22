from itertools import permutations

graph = 'af fc cg gh he ea ed df db hb gb'.split()
matrix = '23 168 158 578 347 27 456 234'.split()

print(*(range(1,9)))
for i in permutations('abcdefgh'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)