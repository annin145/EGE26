from string import printable
from itertools import product
cnt = 0
for val in product(printable[:25], repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        cnt2 = 0
        for i in val:
            if i in printable[:25:2]:
                cnt2 +=1
        if cnt2 == 1:
            cnt1 = 0
            for i in val:
                if i in '012345':
                    cnt1 += 1
            if cnt1 <= 2:
                cnt +=1

print(cnt)


# from itertools import product
# from string import printable
# cnt = 0
# for val in product(printable[:25], repeat=4):
#     val = ''.join(val)
#     if val[0] != 0:
#         cnt1 = 0
#         for i in val:
#             if i in printable[:25:2]:
#                 cnt1 += 1
#         if cnt1 == 1:
#             cnt2 = 0
#             for i in '012345':
#                 cnt2 +=1
#             if cnt2 <= 2:
#                 cnt +=1
# print(cnt)
