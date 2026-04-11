from ipaddress import *

ip1 = ip_address('165.112.200.70')
ip2 = ip_address('165.112.175.80')

for mask in range(16,25):
    net = ip_network(f'{ip1}/{mask}', False)
    if ip1 in net and ip2 in net:
        print(mask)