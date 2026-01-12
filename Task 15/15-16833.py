from itertools import combinations

def f(x):
    p = 25 <= x <= 73
    q = 75 <= x <= 118
    a = a1 <= x <= a2
    return (a and (not q)) <= (p or q)

lineA = [25,73,75,118]
lineX = [30,74,100]

ans = []
for a1,a2 in combinations(lineA,2):
    if all(f(x) for x in lineX):
        ans.append(a2-a1)

print(max(ans))