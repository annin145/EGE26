from ipaddress import *

ip = ip_network('146.180.173.153/255.192.0.0', False)

print(ip[-2])
print(str(max(ip.hosts())).replace('.', ''))
