with open(r'.\files\17_1970.txt') as file:
    data = [int(i) for i in file]

ans = []
for i in range(len(data)-1):
    num1,num2 = data[i:i+2]
    if num1 % 3 == 0 or num2 % 3== 0:
        ans.append(num1+num2)

print(len(ans), max(ans))

#2802 1990