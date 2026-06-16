from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    if ip.count('1') % 2 == 1:
        return 1
    return 0
cnt = 0
net = ip_network('172.16.128.0/255.255.192.0')
for i in net:
    tt = f(i)
    if tt == 1:
        cnt += 1
print(cnt)