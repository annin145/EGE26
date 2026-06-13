from itertools import combinations
def f(x):
    d = 7 <= x <= 68
    c = 29 <= x <= 100
    a = a1 <= x <= a2
    return d <= (((not c) and (not a)) <= (not d))
ans = []
line = [x+eps for x in range(7,101) for eps in (0,0.1,0.9)]
for a1,a2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(a2-a1)

print(min(ans))