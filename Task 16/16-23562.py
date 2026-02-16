from functools import lru_cache

def f(n):
    return g(n-1)

@lru_cache(None)
def g(n):
    if n <= 9: return 3*n
    return g(n-2)+1

for i in range(1,47996):
    g(i)

print(f(47995))