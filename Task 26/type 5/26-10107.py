with open(r'..\files\26_10107.txt') as file:
    N = int(file.readline())
    events = [list(map(int,i.split())) for i in file]

events = sorted(events, key=lambda x: (x[1], x[0]))
f_event = 0
cnt = 0
last_event = []
for event in events:
    if f_event <= event[0]:
        cnt += 1
        f_event = event[1]
        last_event.append(f_event)

print(cnt)

ap = [events[0]]
for event in events:
    if ap[-1][1] <= event[0]:
        ap.append(event)
ap =  ap[:-1]
ap.append(max(events))
print(ap[-1][0] - ap[-2][1])
