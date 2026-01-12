# порядок выполнения операция в алгебре логике
# 1 - отрицание/инверсия - (¬A, (not A))
# 2 - логическое умножение/конъюнкция - (A∧B, A∙B, A and B)
# 3 - логическое сложение/дизъюнкция - (A∨B, A+B, A or B)
# 4 - Следование / Импликация - (A→B, A <= B)
# 5. Тождество / Эквивалентность - (A≡B, A == B)

# порядок выполнения операций в Python
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. in, not in
# 6. ==, !=, >, >=, <, <=
# 7. ^
# 8. not
# 9. and
# 10. or

# решение лесенкой
# print('x y z w')
# for x in range(2):
#     for y in 0,1:
#         for z in (0,1):
#             for w in [0,1]:
#                 f = (not (w<=z)) or (x<=y)or (not x)
#                 # все строки истинны
#                 if f:
#                     print(x,y,z,w)
#                 # все строки ложны
#                 if not f:
#                     print(x,y,z,w)
#                 # строки вперемешку
#                 print(x,y,z,w)

# # args
# def f1(a,b,c):
#     return a + b + c
# test1= [2,5,9]
# print(f1(*test1))

# kwargs
def f2(a,b):
    return a/b
test2 = {'b': 2, 'a' : 5}
print(f2(**test2))

# автокод
from itertools import product, permutations

def f(x,y,z,w):
    return (x or y) and not (y == z) and not w

for i in product((0,1), repeat=4):
    table = [
        (1, i[0], 1, i[1]),
        (0, 1, i[2], 0),
        (i[3],1, 1, 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            # zip(p,t) - сопоставляет заголовки из p с значениями из t;
            # dict(zip(p,t)) - преобразует zip  объект базовый тип данных (словарь);
            # f(**dict(zip(p,t))) - распаковывает через kwargs все ключи в функцию;
            if [f(**dict(zip(p,t))) for t in table] == [1, 1, 1]:
                print(*p, sep='')