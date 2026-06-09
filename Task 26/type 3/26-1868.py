with open(r'..\files\26_1868.txt') as file:
    N = int(file.readline())
    sets = [list(map(int,i.split())) for i in file]
#     rd = [int(i[1]) for i in file]
#     sets = [int(i[0]) for i in file]
#
# sets = sorted(sets)
# rd = sorted(rd)
# f_set = [sets]
# rd = [rd]
# n_set = []
# if max(rd):
#     for sett in sets:
#         if f_set - sett == 3:
#             n_set.append([rd, f_set])
#
# print(n_set)
sets = sorted(sets,key=lambda x: (-x[0], x[1]))

for seat1,seat2 in zip(sets,sets[1:]):
    if seat1[0] == seat2[0]:
        if seat2[1] - seat1[1] == 3:
            print(seat1[0], seat1[1]+1)
            break


