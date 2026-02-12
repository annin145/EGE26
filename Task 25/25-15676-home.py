from fnmatch import fnmatch
from itertools import product

# def prime(x):
#     return x>1 and all(x%d != 0 for d in range(2, int(x**0.5)+1))
#
# for i in range(22768, 10**8, 22768):
#     if fnmatch(str(i), '1*03*6*'):
#         n = str(i)[str(i).index('1')+1:str(i).find('03')]
#         if len(n)>0 and n[0]!='0' and not(prime(int(n))):
#             print(i, n)

##########################################################

def sost(num):
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            return True
    return False

sost_nums = []
for n in range(4, 10_000):
    if sost(n):
        sost_nums += [n]

for i in range(22768, 10**8+1, 22768):
    for n in sost_nums:
        if fnmatch(str(i), f'1{n}03*6*'):
            print(i,n)

###########################################################

ans = []
for l in range(1,5):
    for n in range(10**(l-1), 10**l):
        if sost(n):
            for l2 in range(0, 4 - l + 1):
                for z1 in product('0123456789', repeat=l2):
                    z1 = ''.join(z1)
                    for l3 in range(0, 4- l - l2 + 1):
                        for z2 in product('0123456789', repeat=l3):
                            z2 = ''.join(z2)
                            num = int(f'1{n}03{z1}6{z2}')
                            if num % 22768 == 0 and num < 10**8:
                                ans.append([num,n])
for i in sorted(ans):
    print(*i)

