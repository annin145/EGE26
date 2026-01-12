from itertools import combinations

def f(x):
    p = 1 <= x <= 39
    q = 23 <= x <= 58
    a = a1 <= x <= a2
    return (p <= (not q)) <= (not a)
line = [x + eps for x in range(1,59) for eps in (0,0.1,0.9)]

ans = []
for a1,a2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(a2-a1)

print(max(ans))