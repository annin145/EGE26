with open(r'.\files\17_6791.txt') as file:
    data = [int(i) for i in file]

ans = []
min_n = min(i for i in data if abs(i) % 100 == 68)
for i in range(len(data)-1):
    num1,num2 = data[i:i+2]
    u1 = abs(num1) % 100 == 68
    u2 = abs(num2) % 100 == 68
    if u1+u2 == 1 and num1**2 + num2**2 >= min_n**2:
        ans.append(num1**2 + num2**2)

print(len(ans), max(ans))