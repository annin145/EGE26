from string import printable

for p in printable[:37]:
    num1 = int(f'17496', p)
    num2 = int(f'91f83', p)
    num3 = int(f'd9543', p)
    num = num1 + num2 + num3
    if num % 12 == 0:
        print(p, num // 12)