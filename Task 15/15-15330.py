from itertools import combinations

def f(x):
    b = 24 <= x <= 90
    c = 47 <= x <= 115
    a = a1 <= x <= a2
    return c <= (((not a) and b) <= (not c))

line = [x + eps for x in range(24,116) for eps in(0,0.1,0.9)]

ans = []
for a1,a2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(a2-a1)

print(min(ans))