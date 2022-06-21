from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

cisco3 = {
    'host': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
#    'fast_cli': True,
}

commands = ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']
net_connect = ConnectHandler(**cisco3)

print(datetime.now())
output = net_connect.send_config_set(commands)


print(output)
print(datetime.now())

ping_output = net_connect.send_command('ping google.cim', expect_string='#')

if '!' in ping_output:
    print('DNS success!')
else:
    print(r'No DNS today :(')

print('See...')

print(ping_output)







