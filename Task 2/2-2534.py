from itertools import product,permutations

def f(x,y,z,w):
    return (x == (not y)) <= ((x and w) == (z and(not w)))

for i in product((0,1),repeat=6):
    table = [
        (1,1,i[0], 1),
        (i[1], 1, 1, i[2]),
        (0, i[3], i[4], i[5])
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,t))) for t in table] == [0,0,0]:
                print(*p, sep='')