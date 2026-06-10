from ipaddress import *

ip = ip_network('102.162.200.51/255.255.255.255', False)
print(ip)