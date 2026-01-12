# def convert(num,sys):
#     res = ''
#     while num != 0:
#         res += str(num%sys)
#         num //= sys
#     return res[::-1]
#
# ans = []
# for N in range(1,100_000):
#     R = convert(N,3)
#     if (R.count('1') + (R.count('2')*2)) % 2 == 0:
#         R = '1' + R + '2'
#     else:
#         R = '2' + R + '0'
#     R = int(R,3)
#     if R > 100:
#         ans.append(R)
#
# print(min(ans))



def convert(num,sys):
    res = ''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res [::-1]

ans = []
for N in range(1,100_000):
    R = convert(N,3)
    if (R.count('1') + (R.count('2')*2)) % 2 == 0:
        R = '1' + R + '2'
    else:
        R = '2' + R + '0'
    R = int(R,3)
    if R > 100:
        ans.append(R)

print(min(ans))

