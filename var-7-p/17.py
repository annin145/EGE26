with open(r'.\17_21712.txt') as file:
    data = [int(i) for i in file]
ans = []
min_num = min(i for i in data if i > 0 and len(str(abs(i))) == 4 and i % 10 == 6)
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1 = ((len(str(abs(num1))) == 4) and (num1 % 10 == 6))
    u2 = ((len(str(abs(num2))) == 4) and (num2 % 10 == 6))
    u3 = ((len(str(abs(num3))) == 4) and (num3 % 10 == 6))
    if u1+u2+u3 == 1 and num1+num2+num3 <= min_num:
        ans.append(num1+num2+num3)

print(len(ans),max(ans))