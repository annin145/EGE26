with open(r'.\files\26_4604.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)
boxes = reversed(sorted(boxes))                 # на выбор
boxes = sorted(boxes)[::-1]

last_box = boxes[0]
cnt = 1
for box in boxes:
    if last_box - box >= 3:
        last_box = box
        cnt += 1

print(cnt, last_box)