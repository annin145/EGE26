from itertools import combinations

def f(x):
    p = 15 <= x <= 33
    q = 35 <= x <= 48
    a = a1 <= x <= a2
    return (a and (not q)) <= (p or q)
line = [x + eps for x in range(15,49) for eps in (0,0.1,0.9)]

ans = []
for a1,a2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(a2-a1)

print(max(ans))