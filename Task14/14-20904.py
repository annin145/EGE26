def convert(num,sys):
    res = ''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res [::-1]

for x in range(1, 2031):
    num = 3**100 - x
    num_3 = convert(num,3)
    if num_3.count('0') == 1:
        print(x)

# 1823