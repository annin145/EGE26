from string import printable

for x in printable[:16]:
    num1 = int(f'9{x}ab', 13)
    num2 = int(f'{x}46c', 16)
    num3 = int(f'b7{x}', 15)
    num = num1+num2-num3
    if num % 14 == 0:
        print(x, num // 14)