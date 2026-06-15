from itertools import combinations
def f(x):
    p = 25 <= x <= 64
    q = 40 <= x <= 115
    a = a1 <= x <= a2
    return p <= ((q and (not a)) <= (not p))

line = [x+eps for x in range(25,116) for eps in (0,0.1,0.9)]
ans = []
for a1,a2 in combinations(line,2):
    if all(f(x) for x in range(1,1000)):
        ans.append(a2-a1)

print(min(ans))