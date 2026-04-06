# def convert(num,sys):
#     num = str(num)[::-1]
#     for i in range(len(str(num))):
#         num = int(num[i])*sys**i
#     return num
#
# ans = []
# for x in range(1,9431):
#     num = convert(39**483 + 39**235 - x, 39)
#     r = num.count('0')
#     ans.append(r)
#
# print(max(ans))

ans = []
for x in range(1,9431):
    num = 39**483 + 39**235 - x
    cnt = 0
    while num:
        if num % 39 == 0: cnt += 1
        num //= 39
    ans.append(cnt)

print(max(ans))


