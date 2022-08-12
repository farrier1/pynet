import os
import requests
from pprint import pprint


base_url = 'https://netbox.lasthop.io/api/'
token = os.environ['NETBOX_TOKEN']


http_headers = {
    'accept': 'application/json; version=2.4;',
    'Authorization': f'Token {token}',
}

out = requests.get(f'{base_url}/dcim', headers=http_headers, verify=False)
#out = requests.get('https://netbox.lasthop.io/api/dcim', headers=http_headers, verify=False)


pprint(out.json())

