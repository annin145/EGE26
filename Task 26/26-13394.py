from math import floor, ceil

with open(r'.\files\26.6_13394.txt') as file:
    N = int(file.readline())
    prods = [int(i) for i in file]

prods = sorted(prods, reverse=True)
sale_prods = [i for i in prods if i > 350]


k = 3

many_cheque = sum(prods) - sum(floor(i * 0.75) for i in sale_prods[k-1:k])
one_cheque = sum(prods) - floor(sum(sale_prods[- len(sale_prods) // k:]) * 0.75)

print(many_cheque, one_cheque)
