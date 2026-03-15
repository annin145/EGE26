from itertools import *
def f(x,y,w,z):
    return ((not z) and y and x and (not w)) or ((not z) and y and (not x) and (not w)) or (z and y and x and (not w))

for i in product((0,1), repeat=7):
    table = [
        (i[0],1,i[1],i[2]),
        (i[3], 0,1, i[4]),
        (0,i[5], 0, i[6])
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,t))) for t in table] == [1,1,1]:
                print(*p, sep='')