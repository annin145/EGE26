with open(r'..\files\26_24.txt') as file:
    S,N = map(int, file.readline().split())
    files = [int(i) for i in file]

files = sorted(files)
# print(files)

# summ = 0
# cnt = 0
# max_file = []
# for file in files:
#     if summ + file <= S:
#         summ += file
#         cnt += 1
#         max_file.append(file)

disk = []

for file in files:
    if sum(disk) + file <= S:
        disk.append(file)

disk = disk[:-1]
for file in files[::-1]:
    if sum(disk) + file <= S:
        disk.append(file)
        break
print(len(disk), disk[-1])

