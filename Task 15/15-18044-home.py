from itertools import combinations

def f(x):
    m = 32 <= x <= 68
    n = 54 <= x <= 76
    a = a1 <= x <= a2
    return (not(m or n)) == (not a)

line = [x +eps for x in range(32,77) for eps in (0,0.1,0.9)]

ans = []
for a1,a2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(a2-a1)

print(min(ans))