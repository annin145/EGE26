from string import printable

ans = []
for y in range(9,14):
    for x in range(y+1,14):
        num1 = int(f'7{printable[x]}37{printable[y]}', 14)
        num2 = int(f'9{printable[y]}63', x)
        num3 = int(f'15148', y)
        num = num1 + num2 - num3
        ans.append([num, num // (x+y)])

print(max(ans))
