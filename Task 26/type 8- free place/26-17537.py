with open(r'..\files\26_17537.txt') as file:
    N, M, K = map(int,file.readline().split())
    places = [list(map(int,i.split())) for i in file]

seats = [M] * (K+1)
for row,seat in places:
    seats[seat] = min(seats[seat],row-1)


# for num1,num2 in zip(seats,seats[1:]):
#     if num1 == num2:
#         ans.append([num1,num2])
#     if num1 > num2:
#         ans.append([num2,num1])
#     if num2 > num1:
#         ans.append([num1,num2])

ans = []
for i in range(1, K):
    ans.append([min(seats[i], seats[i+1]), i+1])

print(max(ans))