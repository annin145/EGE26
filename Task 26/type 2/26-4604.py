with open(r'..\files\26_4604.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)
cnt = 1
main_box = boxes[0]
for box in boxes:
    if main_box - box >= 3:
        cnt += 1
        main_box = box

print(cnt, main_box)