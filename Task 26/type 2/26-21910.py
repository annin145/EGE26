with open(r'..\files\26_21910.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes,reverse=True)
cnt = 1
last_box = boxes[0]
for box in boxes:
    if last_box - box >= 9:
        cnt +=1
        last_box = box

print(cnt,last_box)