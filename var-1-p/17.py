with open(r'.\17_23376.txt') as file:
    data = [int(i) for i in file]

ans = []
max_num = max(i for i in data if abs(len(str(i))) == 5 and abs(i) % 100 == 37)
for i in range(len(data)-1):
    num1,num2 = data[i:i+2]
    u1 = (len(str(num1)) == 5)
    u2 = (len(str(num2)) == 5)
    if u1+u2 == 1 and (num1+num2)**2 > max_num**2:
        ans.append(num1+num2)

print(len(ans), max(ans))