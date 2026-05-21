from ipaddress import *

net = ip_network('23.78.143.87/255.255.240.0', False)

print(net)
print(net.num_addresses)