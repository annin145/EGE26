with open(r'.\17_23905.txt') as file:
    data = [int(i) for i in file]
ans = []
max_n = max(i for i in data if i % 100 == 37)
for i in range(len(data)-3):
    nums = n1,n2, n3,n4 = data[i:i+4]
    u2 = []
    u1 = [i > max_n for i in nums]
    for i in nums:
        if len(str(i)) >= 2:
            if str(i)[-1] == str(i)[-2]:
                u2.append(i)
    if sum(u1)==2 and len(u2) == 1:
        ans.append(u2[0])
# print(ans)
print(len(ans),sum(ans))
