f = open('./arp_data.txt', 'r')

arp_data = f.read().splitlines()

del arp_data[0]

arp_data_p = []

for i in arp_data:
    arp_list = i.split()
    arp_dict = {'mac_addr': arp_list[3], 'ip_addr': arp_list[1], 'interface': arp_list[5]}
    arp_data_p.append(arp_dict)

print(arp_data_p)

    


