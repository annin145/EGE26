from itertools import combinations

def f(x):
    p = 10 <= x <= 45
    q = 35 <= x <= 78
    a = a1 <= x <= a2
    return ((not p) <= q) and (not a)

line = [x + eps for x in range(10,79) for eps in(0,0.1,0.9)]

ans = []
for a1,a2 in combinations(line,2):
    if all(not f(x) for x in line):
        ans.append(a2 - a1)

print(min(ans))
