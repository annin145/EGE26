with open(r'..\files\26_17643.txt') as file:
    N = int(file.readline())
    tovars = [list(map(int,i.split())) for i in file]

cr_arif = sum(tovar[1] for tovar in tovars) / N
