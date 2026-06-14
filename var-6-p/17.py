with open(r'.\17_21903 (1).txt') as file:
    data = [int(i) for i in file]
ans = []
min_num = min(i for i in data if abs(i)% 100 == 15 and len(str(abs(i))) == 3)
for num1,num2,num3 in zip(data,data[1:], data[2:]):
    if (num1 == abs(num1) and num2 == abs(num2) and num3 == abs(num3)) or (num1 != abs(num1) and num2 != abs(num2) and num3 != abs(num3)):
        if (max(num1,num2,num3) * min(num1,num2,num3)) > min_num**2:
            ans.append([max(num1,num2,num3) * min(num1,num2,num3)])

print(len(ans), *min(ans))