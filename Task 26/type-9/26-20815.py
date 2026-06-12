with open(r'..\files\26_20815.txt') as file:
    N,K = map(int,file.readline())
    students = []
    for line in file:
        ID, *exs, sob = map(int,line.split())

