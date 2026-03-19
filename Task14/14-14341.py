from string import printable
ans = []
for x in printable[:22]:
    num1 = int(f'56{x}c20',22)
    num2 = int(f'89f{x}2',22)
    num3 = int(f'h24{x}k21',22)
    num = num1+num2+num3
    ans.append(x)


num1 = int(f'560c20',22)
num2 = int(f'89f02',22)
num3 = int(f'h240k21',22)
num0 = num1+num2+num3


print(min(ans),num0//21)
