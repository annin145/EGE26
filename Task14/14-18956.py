from string import printable

ans = []
for x in printable[:15]:
    M = int(f'432{x}3', 15)
    N = int(f'86{x}86', 15)
    for A in range(1, 1_000_000):
        if (M+A) % N == 0:
            ans.append(A)
print(min(ans))

#212298