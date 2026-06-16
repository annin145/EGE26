from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    if ip.count('1') % 5 == 0:
        return 1
    return 0
cnt = 0
net = ip_network('112.160.0.0/255.240.0.0', False)
for i in net:
    tt = f(i)
    if tt == 1:
        cnt += 1
print(cnt)