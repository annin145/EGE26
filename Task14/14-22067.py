from string import printable
def convert(num,sys):
    res = ''
    while num != 0:
        res += printable[num%sys]
        num //= sys
    return res [::-1]

print(printable[:17])
num = 3*17**777 + 15*17**250 - 6*17**100 + 2
num_17 = convert(num,17)
cnt = 0
if num_17.count('0') >= 1:
    cnt += 1
if num_17.count('2') >= 1:
    cnt += 1
if num_17.count('4') >= 1:
    cnt += 1
if num_17.count('6') >= 1:
    cnt += 1
if num_17.count('8') >= 1:
    cnt += 1
if num_17.count('a') >= 1:
    cnt += 1
if num_17.count('c') >= 1:
    cnt += 1
if num_17.count('e') >= 1:
    cnt += 1
if num_17.count('g') >= 1:
    cnt += 1
print(cnt)

# for i in printable[:17:2]:
#     if num_17.count(i) >= 1:
#         cnt += 1
# print(cnt)
