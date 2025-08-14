# псевдослучайные числа

from random import *

# randint() - генерирует одно число на заданном диапозоне
# возвращает int
rnd1 = randint(1, 100)
print(rnd1)

# random() - генерирует одно число от 0 до 1
# возвращает float
rnd2 = random()
print(rnd2)

# choice() - выбирает один случайный элемент из последовательности
rnd3 = choice([1,2,5,3.4])
print(rnd3)

# sample() - выбирает k случайных элементов из последовательности
rnd4 = sample([1,2,5], 3)
print(rnd4)