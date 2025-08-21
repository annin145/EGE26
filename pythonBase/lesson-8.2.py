num = int(input())
mul = 1
while num:
    mul *= num % 10
    num //= 10
print(mul)
