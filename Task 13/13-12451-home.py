from ipaddress import ip_network

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[16:25].count('0') > ip[25:33].count('0')

cnt = 0
for a in range(256):
    net = ip_network(f'246.81.65.{a}/255.255.255.224', False)
    if all(f(ip) for ip in net):
        cnt += 1

print(cnt)