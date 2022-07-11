import pyeapi
from getpass import getpass
import yaml
from my_funcs import read_yaml, print_arp

sw_deets = read_yaml('./arista4.yaml')
connection = pyeapi.client.connect(**sw_deets, password=getpass())
device = pyeapi.client.Node(connection)
arp_entry = device.run_commands('show arp')
arp_entry = arp_entry[0]['ipV4Neighbors']
print_arp(arp_entry)


