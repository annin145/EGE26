with open(r'.\17_29349.txt') as file:
    data = [int(i) for i in file]

cnt = 0
ans = []
min_num = min(i for i in data if i > 0 and i % 123 == 0)
for i in range(len(data)-1):
    num1,num2 = data[i:i+2]
    if num1 + num2 < min_num:
        cnt += 1
        ans.append(num1+num2)
print(cnt, max(ans))