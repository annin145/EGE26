from binascii import a2b_qp
from itertools import combinations

def f(x):
    c = 48 <= x <= 94
    j = 83 <= x <= 100
    a = a1 <= x <= a2
    return (not(c or j)) <= (not a)

lineA = sorted([48,83,94,100])
lineX = [50,90,96]

ans = []
for a1,a2 in combinations(lineA,2):
    if all(f(x) for x in lineX):
        ans.append(a2-a1)

print(max(ans))
