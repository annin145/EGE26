from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 10: return 1
    return (n+3) * f(n-3)

for i in range(1,250_000):
    f(i)

print((f(247563)//519 - 477*f(247560))//f(247557))