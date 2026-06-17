with open(r'.\17_28762.txt') as file:
    data = [int(i) for i in file]

ans = []
min_num = min(i for i in data if i % 23 == 0)
for num1,num2 in zip(data,data[1:]):
    u1 = (num1 % min_num == 0)
    u2 = (num2 % min_num == 0)
    if u1+u2 >= 1:
        ans.append(num1+num2)

print(len(ans), max(ans))