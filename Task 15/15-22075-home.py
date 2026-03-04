def dig(x,y):
    return str(x)[0] == str(y)[0]

def f(x):
    return (not dig(x,28) and dig(x,47)) <= (x > a - 20)

for a in range(1,1000):
    if all(f(x) for x in range(1,1000)):
        print(a)
