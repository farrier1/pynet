import json

ipv4_list = []
ipv6_list = []

with open('nxos_config.json', 'r') as f:
    data = json.load(f)

for k, v in data.items():
    for k1, v1 in v.items():
        if k1 == 'ipv4':
            for k2, v2 in v1.items():
                ipv4_list.append(k2)
                for k3, v3 in v2.items():
                    ipv4_list.append(v3)
        elif k1 == 'ipv6':
            for k2, v2 in v1.items():
                ipv6_list.append(k2)
                for k3, v3 in v2.items():
                    ipv6_list.append(v3)

print(ipv4_list) 
print(ipv6_list)
print('\nIPv4 Addresses: {}\n'.format(ipv4_list))
print('\nIPv6 Addresses: {}\n'.format(ipv6_list))








