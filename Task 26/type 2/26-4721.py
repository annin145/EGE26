with open(r'..\files\26_4712.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes,reverse=True)
cnt = 1
m_box = boxes[0]
for box in boxes:
    if m_box - box >= 3:
        m_box = box
        cnt += 1

print(cnt,m_box)