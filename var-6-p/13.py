from ipaddress import *

for mask in range(16,33):
    ip1 = ip_network(f'153.202.16.37/{mask}', False)
    if ip1.network_address == ip_address('153.202.16.32'):
        print(mask)