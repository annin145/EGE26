with open(r'.\files\17_17530.txt') as file:
    data = [int(i) for i in file]

minn = max(data)
ans = []
for i in range(len(data)-1):
    num1,num2 = data[i:i+2]
    u1 = num1 % 55
    u2 = num2 % 55
    if u1 == minn or u2 == minn:
        ans.append(num1+num2)

print(len(ans), min(ans))