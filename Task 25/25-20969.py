from fnmatch import fnmatch

for n in range(1920368 - 1920368 % 154682, 10**11, 154682):
    if fnmatch(str(n), '*192?3*68'):
        print(n, n//154682)