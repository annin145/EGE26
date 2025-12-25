from itertools import permutations,product

def f(x,y,z):
    return not(x == (y <= z))

for i in product((0,1)):
    table = [
        (0,0,1),
        (0,1,1)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyz'):
            if [f(**dict(zip(p,t))) for t in table] == [1,0]:
                print(*p, sep ='')