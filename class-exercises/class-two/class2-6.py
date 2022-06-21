from netmiko import ConnectHandler
from getpass import getpass
from time import sleep

passwd = getpass()
cisco4 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': passwd,
    'secret': passwd,
    'device_type': 'cisco_ios',
    'session_log': 'my_output.txt',
}


net_connect = ConnectHandler(**cisco4)
print(net_connect.find_prompt())

net_connect.config_mode()
print(net_connect.find_prompt())
net_connect.exit_config_mode()
print(net_connect.find_prompt())

net_connect.write_channel('disable\n')
sleep(2)

output = net_connect.read_channel()
print(output)
net_connect.enable()
print(net_connect.find_prompt())








net_connect.disconnect()






