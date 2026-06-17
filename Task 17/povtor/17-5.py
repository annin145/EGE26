with open(r'.\17_27629.txt') as file:
    data = [int(i) for i in file]
ans = []
max_num = max(i for i in data if len(str(abs(i))) == 4 and i % 100 == 43)
for num1,num2 in zip(data,data[1:]):
    u1 = len(str(abs(num1))) == 4
    u2 = len(str(abs(num2))) == 4
    if u1+u2 >= 1 and (num1+num2)**2 <= max_num**2:
        ans.append((num1+num2)**2)

print(len(ans), max(ans))