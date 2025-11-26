def convert(num,sys):
    res = ''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res[::-1]

for x in range(0,2401):
    num = 7*9**210 + 6*9**110 - x
    num9 = convert(num, 9)
    if num9.count('0') == 100:
        print(x)

# 2394