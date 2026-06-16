from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    if ip.count('1') >= 5:
        return ip
    return 0
ip_2 = ip_address('201.44.240.107')
ip_1 = ip_address('201.44.240.33')
for mask in range(10,31):
    net = ip_network(f'201.44.240.33/{mask}', False)
    if ip_2 in net and f(ip_2) != 0 and f(ip_1) != 0:
        print(mask)