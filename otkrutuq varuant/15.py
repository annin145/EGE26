
from itertools import combinations

def f(x):
    b = 22 <= x <= 40
    c = 32 <= x <= 50
    a = a1 <= x <= a2
    return (not a) <= (b == c)

ans = []
line = [x + eps for x in range(22,51) for eps in (0, 0.1,0.9)]
for a1,a2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(a2-a1)

print(min(ans))