with open(r'..\files\26_6031.txt') as file:
    N = int(file.readline())
    trs = [int(i) for i in file]

trs = sorted(trs, reverse=True)
cnt = 1
trb = [trs[0]]
for tr in trs:
    if trb[-1] - tr >= 6:
        trb.append(tr)
        cnt += 1


print(cnt, trb[-1])