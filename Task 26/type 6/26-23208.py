with open(r'..\files\26_23208.txt') as file:
    N = int(file.readline())
    details = []
    for num, line in enumerate(file, start=1):
        grind, paint = map(int,line.split())
        details.append([grind, 'g', num])
        details.append([paint, 'p', num])

details = sorted(details)
conveyor = [0] * N
last_detail = 0
cnt_g = 0
for detail in details:
    if detail[2] not in conveyor:
        if detail[1] == 'g':
            conveyor[conveyor.index(0)] = detail[2]
            cnt_g += 1
        else:
            conveyor[N - conveyor[::-1].index(0)-1] = detail[2]
        last_detail = detail

print(last_detail[2],cnt_g - 1 if last_detail[1] == 'g' else cnt_g)
#############################################
print()
#############################################
with open(r'..\files\26_23208.txt') as file:
    N = int(file.readline())
    details = []
    for num, line in enumerate(file, start=1):
        grind, paint = map(int,line.split())
        if grind < paint:
            details.append([grind, 'g', num])
        else:
            details.append([paint, 'p', num])

details = sorted(details)
cnt_g = sum(d[1]== 'g' for d in details[:-1])
print(details[-1][2], cnt_g)

