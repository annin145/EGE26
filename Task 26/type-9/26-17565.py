# with open(r'..\files\26_17565.txt') as file:
#     N,S = map(int,file.readline().split())
#
#     candidates = [list(map(int,i.split())) for i in file]
#
# # print(candidates)
# for candidate in candidates:
#     candidates = [candidate[0], candidate[1]+candidate[2]+candidate[3], candidate[4]]
#     ball = [candidate[1]+candidate[2]+candidate[3]],[candidate[0]]
#     ball = sorted(ball)

with open(r'..\files\26_17565.txt') as file:
    N,S = map(int,file.readline().split())
    students = []
    for line in file:
        ID, ex1,ex2,ex3,interview = map(int,line.split())
        students.append([ex1+ex2+ex3, interview, ID])

students = sorted(students, key=lambda x: (-x[0],-x[1],x[2]))

full_score_id = 0
score = 0
cnt_half_score = 0
half_score = students[:S][-1][0]
print(students[:S][0])
if students[:S][-1][0] == students[S:][0][0]:

    cnt_half_score = sum(st[0] == students[:S][-1][0] for st in students)
    full_score_id = [st[2] for st in students if st[0] > half_score][-1]
else:
    score = students[:S][-1][2]

# print(students[:S])
# print()
# print(students[S:])

print(full_score_id, cnt_half_score)
