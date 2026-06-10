with open(r'..\files\26_9756.txt') as file:
    N = int(file.readline())
    events = [list(map(int,i.split())) for i in file]

events = sorted(events, key=lambda x: (x[1], x[0]))

f_event = [events[0]]
for event in events:
    if f_event[-1][1] <= event[0]:
        f_event.append(event)
f_event = f_event[:-1]

for event in events[::-1]:
    if f_event[-1][1] <= event[0]:
        f_event.append(event)
        break

print(len(f_event), f_event[-1][1])

