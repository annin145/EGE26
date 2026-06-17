with open(r'.\17_28938.txt') as file:
    data = [int(i) for i in file]

ans = []
max_num = max(i for i in data if abs(i) % 100 == 28)
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1 = len(str(abs(num1))) == 3
    u2 = len(str(abs(num2))) == 3
    u3 = len(str(abs(num3))) == 3
    if u1+u2+u3 >= 1 and ((num1+num2+num3)/ 3) > 0 and ((num1+num2+num3)/ 3) < max_num:
        ans.append(num1+num2+num3)

print(len(ans), max(ans))