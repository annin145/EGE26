from fnmatch import fnmatch

for n in range(2123406 - 2123406 % 37, 10**8,37):
    if fnmatch(str(n), '2*1234?6'):
        print(n,n//37)