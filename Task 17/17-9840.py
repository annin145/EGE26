with open(r'.\files\17_9840.txt') as file:
    data = [int(i) for i in file]

max_39 = max(i for i in data if i>0 and 1000 <= i <= 9999 and i % 100 == 39)
max_39_2 = max_39**2
ans = []
for i in range(len(data)-1):
    num1,num2 = data[i:i+2]
    u1 = len(str(abs(num1))) == 4
    u2 = len(str(abs(num2))) == 4
    if u1 + u2 == 1 and (num1+num2)**2 <= max_39_2:
        ans.append(num1+num2)

print(len(ans), max(ans))
