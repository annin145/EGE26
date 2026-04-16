# работа с библиотеками

# подключение библиотеки
import random
print(random.randint(1, 100))

# подключение библиотеки через псевдоним
import random as r
print(r.randint(1,10 ))

# подключение одной команды из библиотеки
from random import randint
print(randint(1, 100))

# подключение одной команды из библиотеки через псевдоним
from random import randint as rd
print(rd(1, 100))

# подключение двух команд из библиотеки
from random import randint, choice
print(randint(1, 100), choice([4,3,7,9]))

# подключение двух команд из библиотеки через псевдоним
from random import randint as rd, choice as ch
print(rd(1, 100), ch([1,5,8,4]))

# подключение всех команд из библиотеки
from random import *
print(randint(1, 100), choice([4,3,7,9]))