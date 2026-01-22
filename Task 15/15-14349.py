from itertools import combinations
def f(x):
    b = 54 <= x <= 120
    c = 78 <= x <= 151
    a = a1 <= x <= a2
    return c <= (b and (not a) <= (not c))

line = [x+eps for x in range(54,152) for eps in (0,0.1,0.9)]

ans = []
for a1,a2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(a2-a1)

print(ans)