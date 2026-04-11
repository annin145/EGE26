from ipaddress import ip_network

net = ip_network('205.99.68.249/255.255.248.0', False)

print(list(net.hosts())[-1])

