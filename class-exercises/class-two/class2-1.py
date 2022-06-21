from netmiko import ConnectHandler
from getpass import getpass

cisco4 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
}


net_connect = ConnectHandler(**cisco4)
print (net_connect.find_prompt())

output = net_connect.send_command_timing('ping', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('8.8.8.8', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)


print(output)
 
