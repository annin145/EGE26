from functools import lru_cache
def f(n):
    return g(n-50_000) + g(n+50_000)

@lru_cache(None)
def g(n):
    if n <= 6: return 5**n
    if n > 6: return g(n-3)+2
for i in range(1,1_000_001):
    g(i)
print(f(100_000))