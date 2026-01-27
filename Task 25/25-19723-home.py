from fnmatch import fnmatch

for n in range(1004513 - 1004513 % 451, 10**9, 451):
    if fnmatch(str(n), '10?451*3'):
        print(n,n//451)