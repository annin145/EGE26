with open(r'.\files\26_8512.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

cnt = 0
last_case = 0
case = [0] * K

for time in sorted(times):
    for i in range(K):
        if case[i] < time[0]:
            case[i] = time[1]
            cnt += 1
            last_case = i + 1
            break

print(cnt, last_case)