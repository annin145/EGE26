num = 3*4**38 + 2*4**23 + 4**20 + 3*4**5 + 2*4**4 + 1

num = hex(num)[2:]
num = num.count('0')
print(num)

# 15