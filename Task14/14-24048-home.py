def f(s,p):
    s = s[::-1]
    return sum(int(s[i], 36)* p**i for i in range(len(s)))

for p in range(10,1000):
    if f('KOT', p)+f('GOLODNI', p) == f('MEEOW',p) * f('100', p) - 20194023088:
        print(f('PURR', p))