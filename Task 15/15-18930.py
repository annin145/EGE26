from itertools import combinations

def f(x):
    p = 10 <= x <= 150
    q = 160 <= x <= 250
    r = 240 <= x <= 300
    a = a1 <= x <= a2
    return (q <= p)or((not a) <= r)

line = [x + eps for x in range(10,301) for eps in (0,0.1,0.9)]

ans = []
for a1,a2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(a2-a1)

print(min(ans))