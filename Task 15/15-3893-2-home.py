def d(x,a):
    return x % a == 0

def f(x):
    return d(a,25) and ((d(x,24) and d(x,75)) <= d(x,a))

cnt =0
for a in range(-1000,1000):
    if a and all(f(x) for x in range(-1000,1000)):
        cnt += 1

print(cnt)


