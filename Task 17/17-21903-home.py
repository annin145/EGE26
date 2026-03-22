with open(r'.\files\17_21903.txt') as file:
    data = [int(i) for i in file]

min_kb = min([i for i in data if len(str(abs(i))) == 3 and abs(i) % 100 == 15])**2

ans = []
for i in range(len(data)-2):
    num = num1, num2, num3 =data[i:i+3]
    u = [n > 0 for n in num]
    m = min(num) *max(num)
    if (sum(u)==0 or sum(u)==3) and m > min_kb:
        ans.append(m)

print(len(ans), min(ans))