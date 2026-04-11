with open(r'.\files\26_12113.txt') as file:
    n = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes,reverse=True)

red_tr = [max(i for i in boxes if i % 2 == 1)]
blue_tr = [max(boxes, key=lambda x: ( x % 2 == 0, x ))]

for box in boxes:
    if red_tr[-1] % 2 != box % 2 and red_tr[-1] - box >= 7:
        red_tr.append(box)
    if blue_tr[-1] % 2 != box % 2 and blue_tr[-1] - box >= 7:
        blue_tr.append(box)

print(len(red_tr), red_tr[-1])
print(len(blue_tr), blue_tr[-1])
