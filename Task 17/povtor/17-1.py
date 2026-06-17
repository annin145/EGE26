with open(r'.\17_29971.txt') as file:
    data = [int(i) for i in file]
ans = []
max_num = max(i for i in data if abs(i) % 100 == 33)
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1 = len(str(abs(num1))) == 2
    u2 = len(str(abs(num2))) == 2
    u3 = len(str(abs(num3))) == 2
    if u1+u2+u3 == 2 and (num1+num2+num3)**2 < max_num:
        ans.append(num1+num2+num3)

print(len(ans), max(ans))
