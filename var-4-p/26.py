with open(r'.\26_21598.txt') as file:
    N = int(file.readline())
    times = [list(map(int,i.split())) for i in file]

timeline = [0] * (60 * 24+1)
for time in times:
    for i in range(time[0], time[1]+1):
        timeline[i] += 1
cnt = 0
ans_1 = []
ans_2 = 0

for i in range(1,24*60 - 1 + 1):
    if timeline[i] == timeline[i+1] != 0:
        cnt += 1
    elif timeline[i] != timeline[i+1]:
        ans_1.append(i)
        cnt = 0
    ans_2 = max(ans_2,cnt)

print(ans_1[-2], ans_2)

