from functools import lru_cache

def f(n):
    return 2*(g(n-3)+8)
@lru_cache(None)
def g(n):
    if n < 10: return 2*n
    if n >= 10: return g(n-2)+1

for i in range(1,20_000):
    g(i)
print(f(15_548))