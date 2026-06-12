# with open(r'..\files\26_21719.txt') as file:
#     N = int(file.readline())
#     students = [list(map(int,i.split())) for i in file]
#
# students = sorted(students)
# ID = []
# for student in students:
#     ID.append(student[0])
#
# cnts = [0] * len(ID)
# for cnt in cnts:
#     for student1,student2 in zip(students,students[1:]):
#         if student1[0] == student2[0]:
#             cnt = student2[1] - student1[1]
#
# print(cnts)

#############################################
with open(r'..\files\26_21719.txt') as file:
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
        if tasks[i+1] - tasks[i] == 2:
            cnt += 1
        else:
            cnt = 1
        ans.append([cnt,ID])

print(max(ans, key=lambda x: (x[0], -x[1])))



