import os
import requests
from pprint import pprint


base_url = 'https://netbox.lasthop.io/api/'
token = os.environ['NETBOX_TOKEN']


http_headers = {
    'accept': 'application/json; version=2.4;',
    'Authorization': f'Token {token}',
}

out = requests.get(f'{base_url}dcim/devices/', headers=http_headers, verify=False)


devices = out.json()['results']
for i in devices:
    print('-' * 32)
    print(i['display_name'])
    print('-' * 10)
    print(f'Location: {i["site"]["name"]}')
    print(f'Vendor: {i["device_type"]["manufacturer"]["name"]}')
    print(f'Status: {i["status"]["label"]}')
    print('-' * 32)
    print()




