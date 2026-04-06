with open(r'.\files\17.txt') as file:
    data = [int(i) for i in file]

ans = []
max_2 = max(i for i in data if len(str(i))==2)
for i in range(len(data)-1):
    num1,num2 = data[i:i+2]
    u1 = len(str(num1)) == 2
    u2 = len(str(num2)) == 2
    if u1+u2 == 1 and (num1+num2) % max_2 == 0:
        ans.append(num1+num2)

print(len(ans), max(ans))