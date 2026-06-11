with open(r'..\files\26_9847.txt') as file:
    N = int(file.readline())
    guests = [list(map(int,i.split())) for i in file]

# cnt = 0
# ans = 0
# time = [0,0]
# for i in range(1440):
#     for guest in guests:
#         if guest[0] == i:
#             cnt += 1
#             ans = max(ans,cnt)
#             time = [guest[0], guest[1]]
#         if guest[1] == i:
#             cnt -= 1
#
# print(time,ans)

timeline = [0] *60 *24
for guest in guests:
    for i in range(guest[0],guest[1]):
        timeline[i] += 1

# print(max(timeline))
max_cnt = max(timeline)
ans1 = []
for i in range(len(timeline)):
    if timeline[i] == max_cnt:
        ans1.append(i)

cnt1 = 1
for num1,num2 in zip(ans1,ans1[1:]):
    if num2 - num1 > 1:
        cnt1 += 1
print(cnt1,max_cnt)


