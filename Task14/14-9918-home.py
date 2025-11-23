from string import printable

for x in printable[:67]:
    for y in printable[:66]:
        num1 = int(f'73{x}1{y}', 67)
        num2 = int(f'49{y}6', x)
        num = num1 + num2
    print(x, y)