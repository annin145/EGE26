def f(start,steps):
    if steps == 13: return {start}
    return f(start-3,steps+1) | f(start*(-3),steps+1)

b = f(333,0)

cnt = 0
for i in b:
    if i < 0:
        cnt += 1

print(cnt)