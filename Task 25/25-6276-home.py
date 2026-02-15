from fnmatch import fnmatch

for n in range(10101011 - 10101011 % 2023, 10**10, 2023):
    if sum(map(int,str(n))) == 22:
        if fnmatch(str(n), '1?1?1?1*1'):
            print(n)