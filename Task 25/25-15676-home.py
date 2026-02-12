from fnmatch import fnmatch

def prime(x):
    return x>1 and all(x%d != 0 for d in range(2, int(x**0.5)+1))

for i in range(22768, 10**8, 22768):
    if fnmatch(str(i), '1*03*6*'):
        n = str(i)[str(i).index('1')+1:str(i).find('03')]
        if len(n)>0 and n[0]!='0' and not(prime(int(n))):
            print(i, n)