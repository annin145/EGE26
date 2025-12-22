from itertools import *

for pos1, val1 in enumerate(product('конец', repeat=5), start=1):
    val1 = ''.join(val1)

for pos2, val2 in enumerate(product('дракон', repeat=5), start=1):
    val2 = ''.join(val2)

for pos3, val3 in enumerate(product('кон', repeat=5), start=1):
    val3 = ''.join(val3)

pos = pos1 + pos2 - pos3 -pos3
print(pos)

#10415