with open(r'.\files\26.2_19727.txt') as file:
    s,n = map(int, file.readline().split())
    milks = [int(i) for i in file]

milks = sorted(milks)
ans = []
for milk in milks:
    if sum(ans) + milk <= s:
        ans.append(milk)

V_ost = s - sum(ans[:-1])


print(len(ans), )