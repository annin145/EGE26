with open(r'.\17_21416.txt') as file:
    data = [int(i) for i in file]

ans = []
nums = sum([i for i in data if i != abs(i)])
for num1,num2,num3 in zip(data,data[1:], data[2:]):
    if (max(num1,num2,num3)*min(num1,num2,num3)) > nums:
        ans.append(num1+num2+num3)

print(len(ans), max(ans))