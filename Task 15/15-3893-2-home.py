def d(x,a):
    return x % a == 0

def f(x):
    return d(abs(a),25) and (d(abs(x),24) and d(abs(x),75) <= d(abs(x),a))

cnt =0
for a in range(-1000,1000):
    if all(f(x) for x in range(-1000,1000)):
        cnt += 1

print(cnt)


