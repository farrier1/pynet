import json

arp_list = {}

with open('arista_config.json', 'r') as f:
    data_raw = json.load(f)

arp = data_raw['ipV4Neighbors']

for k in arp:
    arp_list[k['address']]= k['hwAddress']

print(arp_list)








