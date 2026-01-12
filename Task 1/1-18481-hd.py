from itertools import *

graph = 'ac ce eg gf fd db ba bc de'.split()
martix = '67 567 457 35 234 12 123'.split()

print(*(range(1,9)))
for i in permutations('abcdefg'):
    if all(str(i.index(x)+1) in martix[i.index(y)] for x,y in graph):
        print(*i)
