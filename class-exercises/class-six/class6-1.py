import pyeapi
from getpass import getpass
import yaml

with open('./arista4.yaml', 'r') as f:
    sw_deets = yaml.safe_load(f)

connection = pyeapi.client.connect(**sw_deets, password=getpass())

'''
Or use a local dict

connection = pyeapi.client.connect(
    transport='https',
    host='arista3.lasthop.io',
    username='pyclass',
    password=getpass(),
    port='443',
)
'''

device = pyeapi.client.Node(connection)

arp_entry = device.run_commands('show arp')
arp_entry = arp_entry[0]['ipV4Neighbors']


for n in arp_entry:
    print('IP Address: {address} HW Address: {hwAddress}'.format(**n))   





'''
{'hwAddress': '0024.c4e9.48ae',
 'address': '10.220.88.1',
 'interface': 'Vlan1, Ethernet1',
 'age': 0}
''' 

