from netmiko import ConnectHandler
from getpass import getpass

cisco4 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
}


net_connect = ConnectHandler(**cisco4)

output = net_connect.send_command_timing('show lldp neighbors', use_textfsm=True)

output_dict = output[0]
print('Neighbour Interface: ', output[0]['neighbor_interface'])

 
