with open(r'.\17_16383.txt') as file:
    data = [int(i) for i in file]
ans = []
max_num = max(i for i in data if i % 100 ==21 and len(str(i)) == 5)
for i in range(len(data)-1):
    num1,num2 = data[i:i+2]
    u1 = len(str(abs(num1)%100==21)) == 5
    u2 = len(str(abs(num2)%100==21)) == 5
    if u1+u2 == 1 and (num1+num2)**2 >= max_num**2:
        ans.append(num1+num2)

print(len(ans),max(ans))

# test = 10_001
# print(test//100_000)
