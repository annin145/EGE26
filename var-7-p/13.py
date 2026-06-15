from ipaddress import *

ip = ip_network('98.81.154.195/255.252.0.0', False)

print(ip[-2])