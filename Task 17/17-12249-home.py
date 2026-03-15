with open(r'.\files\17_12249.txt') as file:
    data = [int(i) for i in file]

maxx = max(data)
ans = []
for i in range(len(data)-2):
    num1, num2, num3 =sorted([data[i], data[i + 1], data[i + 2]])
    if str(num1)[-1:] == '3' or str(num2)[-1:] == '3' or str(num3)[-1:] == '3':
        if num1+num2+num3 < maxx:
            ans.append(num1+num2+num3)

print(len(ans), max(ans))
#1767 99081
