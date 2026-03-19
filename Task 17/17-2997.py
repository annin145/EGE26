with open(r'.\files\17_2997.txt') as file:
    data = [int(i) for i in file]

nums_3 = [int(str(abs(i))[1]) for i in data if 100 <= abs(i) <= 999]
most_common = max((nums_3.count(i),i) for i in range(10))[1]

ans = []
for i in range(len(data)-1):
    num1,num2 = data[i:i+2]
    u1 = abs(num1) % 10 == most_common
    u2 = abs(num2) % 10 == most_common
    if u1+u2 >= 1:
        ans.append(num1+num2)

print(len(ans), max(ans))
