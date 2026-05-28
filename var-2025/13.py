from ipaddress import *

ip = ip_network('205.99.68.249/255.255.248.0', False)
# ip = ip.hosts()
print(ip.broadcast_address)