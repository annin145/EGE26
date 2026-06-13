with open(r'.\17_17558.txt') as file:
    data = [int(i) for i in file]

ans = []
nums_32 = [i for i in data if abs(i) % 32 == 0]
for num1,num2 in zip(data,data[1:]):
    u1 = abs(num1) != num1
    u2 = abs(num2) != num2
    if u1+u2 >= 1 and num1+num2 < len(nums_32):
        ans.append(num1+num2)

print(len(ans), max(ans))