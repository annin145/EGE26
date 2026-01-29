from fnmatch import fnmatch

for n in range(1021394 - 1021394 % 3052, 10**10, 3052):
    if fnmatch(str(n), '1?2139*4'):
        print(n, n // 3052)