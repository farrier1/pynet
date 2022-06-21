from pprint import pprint
import yaml



cisco3 = {"device_name": "cisco3", "host": "cisco3.lasthop.io", "username": "user", "password": "pass"}

cisco4 = {"device_name": "cisco4", "host": "cisco4.lasthop.io", "username": "user", "password": "pass"}

arista1 = {"device_name": "arista1", "host": "arista1.lasthop.io", "username": "user", "password": "pass"}

arista2 = {"device_name": "arista2", "host": "arista2.lasthop.io", "username": "user", "password": "pass"}

devices = [cisco3, cisco4, arista1, arista2]

with open('device_list_ext.yml', 'w') as f:
    yaml.dump(devices, f, default_flow_style=False)









