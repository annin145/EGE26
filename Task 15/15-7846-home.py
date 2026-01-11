from itertools import combinations

def f(x):
    p = 13 <= x <= 19
    q = 17 <= x <= 23
    a = a1 <= x <= a2
    return (not((not p) <= q)) <=(a <= ((not q) <= p))

line = [x + eps for x in range(13,24) for eps in(0,0.1,0.9)]

ans = []
for a1,a2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(max(ans))

