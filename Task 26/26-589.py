with open(r'.\files\26_589.txt') as file:
    N = int(file.readline())
    prises = [int(i) for i in file]

prises = sorted(prises)

# for n in range(20):
#     ans_n = []
# print(max(prises))
# for i in prises:
#     if i // 500 == n:
#         ans_n.append(i)
#
# print(ans_n)

groups = []
sum_sales = 0
max_sales = 0
for i in range(0, max(prises), 500):
    group = [ j for j in prises if i * 500 < j <= i+ 500]
#    sale_cnt = len(group) // 2
    sale = sum(group[:len(group) // 2]) / 2
    max_sales = max(max_sales, max(group[:len(group) // 2]))

print(sum_sales, max_sales /2)
