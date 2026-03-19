with open(r'.\files\17_11236.txt') as file:
    data = [int(i) for i in file]

kb_min = min(i for i in data if 9 < abs(i) < 100) ** 2
max_num = max(n for n in data if 999 < abs(n) < 10_000 and abs(n) % 10 == 1)

ans = []
for i in range(len(data)-2):
    num1,num2,num3 = data[i:i+3]
    u1 = num1 > kb_min
    u2 = num2 > kb_min
    u3 = num3 > kb_min
    if u1+u2+u3==2 and abs(num1)*abs(num2)*abs(num3) % abs(max_num) == 0:
        ans.append(abs(num1)+abs(num2)+abs(num3))

print(len(ans),max(ans))