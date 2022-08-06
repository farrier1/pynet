from my_devices import net_things
from napalm import get_network_driver



def connection(device):
    device_type = device.pop('device_type')
    driver = get_network_driver(device_type)
    host = driver(**device)
    host.open()
    return host



for i in net_things:
    connect = connection(i)
    output = connect.get_facts()
    print(output)

print('All done')

