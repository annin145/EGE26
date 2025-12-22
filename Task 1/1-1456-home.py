from itertools import permutations

graph = 'аб бе еж жд дв ва аг гб гв гд де'.split()
matrix = '256 13467 2456 237 136 1235 24'.split()

print(*(range(1,9)))
for i in permutations('абвгдеж'):
    if all(str(i.index(x) +1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# в д б е а г ж