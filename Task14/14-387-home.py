num = 51*7**12 - 7**3 - 22

def convert(num,sys):
    res = ''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res[::-1]
num_1 = convert(num, 7)
num_1 = sum(map(int,num_1))

print(num_1)

#70
