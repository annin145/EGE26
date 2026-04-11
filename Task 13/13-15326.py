from ipaddress import *

net = ip_network('105.224.200.224/255.255.255.224', False)

cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 4 == 0:
        cnt += 1

print(cnt)