# from ipaddress import ip_network
#
# net = ip_network('172.140.68.0/255.255.248.0')
#
# cnt = 0
# for ip in net:
#     ip = f'{int(ip):032b}'
#     if ip.count('0') > 15:
#         cnt += 1
#
# print(cnt)

# 128.192.0.128
# 1000000.11000000.00000000.10000000

# 128.192.0.34
# 10000000.11000000.00000000.00100010

print(bin(255))