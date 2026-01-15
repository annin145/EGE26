# def expr(x, A):
#     return (x % A == 0) or ((70 <= x <= 90) <= (not (x % 22 == 0)))
#
# for A in range(1000,0,-1):
#     if all(expr(x, A) for x in range(1, 10_000)):
#         print(A)
#         break


def f(a):
    for x in range(0, 1000):
        b = 70 <= x <= 90
        F = (x % a == 0) or (b <= (x % 22 != 0))
        if not F:
            return False
    return True


for a in range(1, 1000):
    if f(a):
        print(a)