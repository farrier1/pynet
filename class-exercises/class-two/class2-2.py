from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime 

cisco2 = {
    'host': 'cisco2.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
#    'global_delay_factor': 2
}


net_connect = ConnectHandler(**cisco2)
start = datetime.now()
output = net_connect.send_command('show lldp neighbors detail', delay_factor = 8)

finish = datetime.now()

print(output)
print('-' * 20)
print('Start time: ', start)
print('Finish time :', finish)
 
