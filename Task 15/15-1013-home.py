from itertools import combinations

def f(x):
    p = 23 <= x < 45
    q = 34 <= x <= 56
    a = a1 <= x <= a2
    return (not a) or (not p) and q
line = [x + eps for x in range(23,57) for eps in (0,0.1,0.9)]

ans = []
for a1,a2 in combinations(line,2):
    if all(f(x)for x in line):
        ans.append(a2-a1)

print(max(ans))
