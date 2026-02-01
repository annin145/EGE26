def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

for x in range(1,100):
    num = 7**666 + 7**333 +49**x - 343
    num7 = convert(num,7)
    if num7.count('6') == 49:
        print(x)