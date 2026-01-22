from string import printable

for x in printable[1:8]:
    num1 = int(f'{x}1{x}',16)
    num2 = int(f'{x}3{x}3',8)
    num = num1 + num2
    for i in range(0,1000):
        if num == 2**i:
            print(x)

# from math import log2
# if log2(num) % 1 == 0 or log2(4) == int(log2(4)) or str(log2(num))[-1] == '0':