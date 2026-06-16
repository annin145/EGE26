#28936

# def f(x,y):
#     return (x*y < a) or (5*x < y) or (486 <= x)
#
# for a in range(0,10000):
#     if all(f(x,y) for x in range(1,10000) for y in range(1,10000)):
#         print(a)
#         break

# print(486*5)
# print(485*5*485+1)

# 27770
def DEL(n,m):
    return n % m == 0

def f(x):
    return DEL(x,21) <= ((not DEL(x,a)) <= (not(DEL(x,77))))

for a in range(1,1000)[::-1]:
    if all(f(x) for x in range(1,1000)):
        print(a)
        break

print(7*3*11)
