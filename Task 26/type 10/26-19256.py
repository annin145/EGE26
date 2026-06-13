with open(r'..\files\26_19256.txt') as file:
    N = int(file.readline())
    students = {}
    for line in file:
        ID, task = map(int,line.split())
        if ID not in students:
            students[ID] = {task}
        else:
            students[ID] |= {task}

ans = []
cnt = 1
for ID in students:
    tasks = sorted(students[ID])
    for i in range(len(tasks)-1):
        if tasks[i+1] - tasks[i] == 1:
            cnt += 1
        else:
            cnt = 1
        ans.append([cnt,ID])

print(min(ans, key=lambda x: (x[0], -x[1])))