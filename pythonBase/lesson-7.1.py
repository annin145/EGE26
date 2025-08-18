#1
#num = int(input())

#if num % 10 == 0 or num % 10 == 5 or num % 10 == 2:
#    print(num)
#else:
#    print(num + 1)

#2
# if num > 0:
#     print(num + 1)
# else:
#     print(num - 1)

# num += 1 if num > 0 else - 1
# print(num)

#3
from random import randint
num = randint(0, 100)
print(num)

if num % 3 == 0:
    print(num / 3)
else:
    print(num * 2)

#print(num / 3 if num % 3 == 0 else num * 2)

num /= 3 if num % 3 == 0 else 1 / 2
print(num)