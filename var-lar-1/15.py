from itertools import combinations
def f(x):
    c = 25 <= x <= 64
    t = 50 <= x <= 120
    a = a1 <= x <= a2
    return (not(c <= a)) <= t

line = [x + eps for x in range(25,121) for eps in(0,0.1,0.9)]
ans = []
for a1,a2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(a2-a1)

print(min(ans))