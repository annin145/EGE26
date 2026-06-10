with open(r'.\17_23276.txt') as file:
    data = [int(i) for i in file]

ans = []
max_num = max(i for i in data if i % 100 == 25)
for i in range(len(data)-2):
    num1,num2,num3 = data[i:i+3]
    if len(str(num1)) == 4 and len(str(num2)) == 4 and len(str(num3)) ==4:
        if num1+num2+num3 <= max_num:
            ans.append(num1+num2+num3)

print(len(ans), max(ans))