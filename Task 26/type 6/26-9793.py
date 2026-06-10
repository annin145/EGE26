with open(r'..\files\26_9793.txt') as file:
    N = int(file.readline())
    pieces = []
    for pos,data in enumerate(file, start=1):
        time_1,time_2 = map(int,data.split())
        pieces.append([time_1,'s', pos])
        pieces.append([time_2,'o', pos])

pieces = sorted(pieces)
conveyor = [0] *N
left, right = 0,N-1
last_pieces = 0
cnt = 0
for piece in pieces:
    if piece[2] in conveyor:
        continue
    if piece[1] == 's':
        conveyor[left] = piece[2]
        left += 1
        cnt += 1
    else:
        conveyor[right] = piece[2]
        right -= 1
    last_pieces = piece

print(last_pieces[2], cnt -1 if last_pieces[1] == 's' else 0)
#############################################################################
with open(r'..\files\26_9793.txt') as file:
    N = int(file.readline())
    pieces = []
    for pos, data in enumerate(file, start=1):
        time_1, time_2 = map(int, data.split())
        if min(time_1, time_2) == time_1:
            pieces.append([time_1, 's', pos])
        else:
            pieces.append([time_2, 'o', pos])

pieces = sorted(pieces)

last_piece = pieces[-1]
cnt = sum(1 for piece in pieces if piece[1] == 's')

print(last_piece[2], cnt - 1 if last_piece[1] == 's' else 0)






# detls_v = []
# for detl in zip(detls, detls[1:]):
#     if detl[1] > detl[0]:
#         detls_v.append([detl[0], detl[1]])
#     else:
#         detls_v.append([detl[1], detl[0]])
#
# detls_v = sorted(detls_v)
# print(detls_v)


# # print(detls)
# places = [0] *N
# for detl in detls:
#     for i in range(N):
#         if min(*detl) == i:
#             places.append(detl)
#             break
#
# print(places)
# print(detls)


# d = max(detls, key=lambda x: x[1])
# print()
# cnt = 0
# for i in range(N):
#     if i != d:
#         cnt +=1
# print(d)
# print(cnt)



