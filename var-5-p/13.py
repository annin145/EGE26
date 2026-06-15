from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip.count('1') % 4 == 0 and ip[-2:] == '11'

ip = ip_network('211.46.0.0/255.255.128.0', False)

cnt = 0
for i in ip:
    if IP := f(i):
        cnt += 1

print(cnt)