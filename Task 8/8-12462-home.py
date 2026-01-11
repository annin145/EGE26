cnt = 0

for val1 in range(1, 16):
    for val2 in range(0, val1):
        for val3 in range(0, val2):
            cnt += 1

for vall1 in range(1, 16):
    for vall2 in range(0, vall1):
        for vall3 in range(0, vall2):
            for vall4 in range(0, vall3):
                for vall5 in range(0, vall4):
                    cnt += 1
print(cnt)