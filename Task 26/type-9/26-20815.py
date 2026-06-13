with open(r'..\files\26_20815.txt') as file:
    N,K = map(int,file.readline())
    students = []
    for line in file:
        ID, *exs, sob = map(int,line.split())
        students.append([sum(exs), sob, ID])

students = sorted(students, key=lambda x: (-x[0], -x[1], x[2]))
score = 0
half_score = 0
full_score_id = 0
half_score_students = students[:K][-1][0]

if students[:K][-1][0] == students[K:][0][0]:
    half_score = sum(st[0] == students[:K][-1][0] for st in students)
    full_score_id = [st[2] for st in students if st[0] > half_score][-1]
else:
    score = students[:K][-1][2]