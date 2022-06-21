import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

with open('./.netmiko.yml', 'r') as f:
    config_data = yaml.safe_load(f)

device = config_data['cisco4']

net_connect = ConnectHandler(**device)

config = net_connect.send_command('show run')

parsed = CiscoConfParse(config.splitlines(), factory=True)

ip_addresses = parsed.find_objects_w_child(parentspec=r'^interface', childspec=r'^ ip address')

for int in ip_addresses:
    print('Interface Line: ', int.text)
    for child in int.children:
        if 'ip address' in child.text:
            print('IP Address Line: ', child.text)










