from itertools import combinations
def f(x):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2
    return p <= ((q and (not a)) <= (not p))

line_a = [15,21,40,63]
line_x = [16,22,41]
ans = []
for a1,a2 in combinations(line_a,2):
    if all(f(x) for x in line_x):
        ans.append(a2-a1)

print(min(ans))