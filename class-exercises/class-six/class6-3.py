import pyeapi
from getpass import getpass
import yaml
from my_funcs import read_yaml

connected = []
static = []

sw_deets = read_yaml('./arista4.yaml')
connection = pyeapi.client.connect(**sw_deets, password=getpass())
device = pyeapi.client.Node(connection)

sho_route = device.run_commands('show ip route')
routes = sho_route[0]['vrfs']['default']['routes']

for k in routes:
    if routes[k]['routeType'] == 'connected':
        connected.append(k)
    elif routes[k]['routeType'] == 'static':
        static.append(k)
print()
print('Static Routes')
print('-' * 7)
print(static)
print()
print('Connected Routes')
print('-' * 16)
print(connected)
print()



