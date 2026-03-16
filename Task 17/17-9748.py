with open(r'.\files\17_9748.txt') as file:
    data = [int(i) for i in file]

max_15 = max(i for i in data if i % 100 == 15)
ans = []
for i in range(len(data)-2):
    num1, num2, num3 = data[i:i+3]
    u1 = 1000 <= num1 <= 9999
    u2 = 1000 <= num2 <= 9999
    u3 = 1000 <= num3 <= 9999
    if num1+num2+num3 >= max_15 and u1+u2+u3 == 1:
        ans.append(num1+num2+num3)

print(len(ans), max(ans))

