# системы счисления

# двоичная система
N = 25
print(bin(N))
print(bin(N)[2:]) #bin() - переводит десятичное число в двоичную систему
# принимает на вход int, возвращает str
# [2:]- срез убирающие 2 символа '0b'
print(f'{N:b}') # f'' - форматируемая строка, которая позволяет вставлять в себя переменные

# восьмеричная система
print(oct(N)[2:])
print(f'{N:o}')

# шестнадцатеричная система
print(hex(N)[2:])
print(f'{N:x}')

# перевод в любую систему счисления (2 <= sys <= 9)
def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

print(convert(25,8))

# Перевод в любую систему счисления (2 <= sys <= 36)
from string import printable

def convert2(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

# срезы
test = 'Hello,world!'
#  извлечение первых двух символов
print(test[:2])
# строка без первых двух символов
print(test[2:])
# извлечение последних двух символов
print(test[-2:])
# строка без последних двух символов
print(test[:-2])

