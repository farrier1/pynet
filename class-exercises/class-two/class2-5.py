from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

passwd = getpass()
nxos1 = {
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': passwd,
    'device_type': 'cisco_nxos',
}

nxos2 = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': passwd,
    'device_type': 'cisco_nxos',
}

device_list = [nxos1, nxos2]

for i in device_list:
    net_connect = ConnectHandler(**i)
    output = net_connect.send_config_from_file('./vlan-changes.txt')
    wr_mem = net_connect.save_config()
    print(output)









