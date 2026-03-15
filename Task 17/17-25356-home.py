with open(r'./files/17_25356.txt') as file:
    data = [int(i) for i in file]

M = None
for num in data:
    if abs(num) % 100 == 30:
        if M is None or abs(num) > abs(M):
            M = num

ans = []
for i in range(len(data) - 2):
    num = num1,num2,num3 = sorted([data[i], data[i+1],data[i+2]])
    u1 = 1000 < num1 < 9999
    u2 = 1000 < num2 < 9999
    u3 = 1000 < num3 < 9999
    if (not u1) and (not u2) and (not u3) and num1+num2+num3 >= M:
        ans.append(num1+num2+num3)

print(len(ans), max(ans))