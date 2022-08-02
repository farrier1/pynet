import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

pword = getpass()

device = Device(
    api_format='jsonrpc',
    host='nxos1.lasthop.io',
    username='pyclass',
    password=pword,
    transport='https',
    port=8443,
    verify=False,
)

xml_device = Device(
    api_format='xml',
    host='nxos1.lasthop.io',
    username='pyclass',
    password=pword,
    transport='https',
    port=8443,
    verify=False,
)

output = device.show('show interface Ethernet1/1')

output = output['TABLE_interface']['ROW_interface']

interface = output['interface']
admin_state = output['admin_state']
mtu = output['eth_mtu']

print()
print('6a:')
print(f'Interface: {interface}; State: {admin_state}; MTU: {mtu}')
print()

xml_output = xml_device.show('show interface Ethernet1/1')

xml_interface = xml_output.find('.//interface').text
xml_admin_state = xml_output.find('.//admin_state').text
xml_mtu = xml_output.find('.//eth_mtu').text

print()
print('7a:')
print(f'Interface: {xml_interface}; State: {xml_admin_state}; MTU: {xml_mtu}')
print()

print('7b: Multi show commands')
commands = ['show system uptime', 'show system resources']

xml_moutput = xml_device.show_list(commands)
for e in xml_moutput:
    print(etree.tostring(e).decode())
print()

cfg_commands = ['interface loopback 99', 'description 99', 'interface loopback 100', 'description 100']

xml_coutput = xml_device.config_list(cfg_commands)
for i, e in enumerate(xml_coutput):
    print(etree.tostring(xml_coutput[i]).decode())

























