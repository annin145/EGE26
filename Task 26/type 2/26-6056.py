with open(r'..\files\26_6056.txt') as file:
    N = int(file.readline())
    trbs = [int(i) for i in file]

trbs = sorted(trbs, reverse=True)
cnt = 1
m_trb = trbs[0]
for trb in trbs:
    if m_trb - trb >= 56:
        cnt += 1
        m_trb = trb

print(cnt,m_trb)
