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

output = net_connect.send_command('ping', expect_string=r'ip')
output += net_connect.send_command('\n', expect_string=r'address')
output += net_connect.send_command('8.8.8.8', expect_string=r'5')
output += net_connect.send_command('\n', expect_string=r'100')
output += net_connect.send_command('\n', expect_string=r'2')
output += net_connect.send_command('\n', expect_string=r'n')
output += net_connect.send_command('\n', expect_string=r'n')
output += net_connect.send_command('\n', expect_string=r'n')


print(output)
 
