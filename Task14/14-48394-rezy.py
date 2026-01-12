from string import printable

for x in printable[:15]:
    num1 = int(f'4c{x}4', 15)
    num2 = int(f'{x}62A',13)
    num = num1 + num2
    if num % 121 == 0:
        print(x, num // 121)

a = [int(f'4C{x}4',15)+int(f'{x}62A',13) for x in '123456789']
print(min([n for n in a if n%121==0])//121)