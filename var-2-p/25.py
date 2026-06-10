from fnmatch import fnmatch

for n in range(1230056 - 1230056%171,10**8, 171):
    if fnmatch(str(n), '1*23??56'):
        print(n,n//171)