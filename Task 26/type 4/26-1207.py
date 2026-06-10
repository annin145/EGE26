with open(r'..\files\26_1207.txt') as file:
    S,N = map(int, file.readline().split())
    files = [int(i) for i in file]

files = sorted(files)

disk = []
for file in files:
    if sum(disk) + file <= S:
        disk.append(file)

disk = disk[:-1]
for file in files[::-1]:
    if sum(disk) + file <= S:
        disk.append(file)
        break

print(len(disk),disk[-1])
