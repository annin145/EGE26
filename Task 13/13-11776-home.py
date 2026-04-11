from ipaddress import ip_network

net = ip_network('235.86.56.0/255.255.248.0', False)

cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip[-2] == '11':
        cnt += 1

print(cnt)

from ipaddress import *
k = 0
network = ip_network(f'235.86.56.0/255.255.248.0')
for ip in network:
   if f'{ip:b}'[-2:] == '11':
        k += 1
print(k)