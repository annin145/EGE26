# from string import printable
#
# for x in printable[:67]:
#     for y in printable[:66]:
#         num1 = int(f'73{x}1{y}', 67)
#         num2 = int(f'49{y}6', x)
#         num = num1 + num2
#     print(x, y)

ans = []

for y in range(67):
    for x in range(max(10,y +1), 67):
        num1 = 7*67**4 + 3*67**3 + x*67**2 + 1*67**1 + y*67**0
        num2 = 4*x**3 + 9*x**2 + y*x**1 + 6*x**0
        num = num1 + num2
        ans.append(num)

print(len(set(ans)))