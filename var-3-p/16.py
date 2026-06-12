from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 17: return 6
    if n >= 17: return (n+5)*f(n-9)

for i in range(2500,234600):
    f(i)
print((f(234561//436+f(234552)//218))//f(234534))

# не запускать!!!!!!!