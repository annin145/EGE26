from itertools import combinations

def f(x):
    p = 66 <= x <= 67
    o = 32 <= x <= 125
    t = 30 <= x <= 491
    a = a1 <= x <= a2
    return (not a) <= (p or (not o) or (not t))

line = [x+eps for x in range(30,492) for eps in (0,0.1,0.9)]

ans = []
for a1,a2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(a2-a1)

print(min(ans))