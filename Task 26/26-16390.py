with open(r'.\files\26_16390 (1).txt') as file:
    s,n = map(int, file.readline().split())
    boxes = [int(i) for i in file]

boxes = sorted(boxes)

ans = []
for box in boxes:
    if sum(ans) + box <= s:
        ans.append(box)

ans = ans[:-1]
V_ost = s - sum(ans)

print(len(ans)+1, max(i for i in boxes if i <= V_ost))