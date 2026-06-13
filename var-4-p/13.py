from ipaddress import *

for x in range(24,33):
    ip = ip_network(f'172.16.168.0/255.255.255.{x}', False)

print(ip_address())