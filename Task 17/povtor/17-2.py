with open(r'.\17_29349.txt') as file:
    data = [int(i) for i in file]
ans = []
min_num = min(i for i in data if i > 0 and i % 123 == 0)
for num1,num2 in zip(data,data[1:]):
    if (num1+num2) < min_num:
        ans.append(num1+num2)

print(len(ans), max(ans))