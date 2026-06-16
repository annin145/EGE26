from ipaddress import *

ip = ip_network('68.203.243.87/255.255.224.0', False)

print(ip[-2])
print(68+203+255+254)