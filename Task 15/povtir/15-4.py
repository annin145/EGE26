from itertools import combinations
def f(x):
    b = 36 <= x <= 75
    c = 60 <= x <= 110
    a = a1 <= x <= a2
    return (not a) <= (b == c)

# line = [x+eps for x in range(36,101) for eps in (0,0.1,0.9)]
line_a = [36,60,75,110]
line_x = [36,61,76]
ans = []
for a1,a2 in combinations(line_a,2):
    if all(f(x) for x in line_x):
        ans.append(a2-a1)

print(min(ans))
