import os
import requests
from pprint import pprint
import json

base_url = 'https://netbox.lasthop.io/api/'
token = os.environ['NETBOX_TOKEN']


http_headers = {
    'Content-Type': 'application/json; version=2.4;',
    'accept': 'application/json; version=2.4;',
    'Authorization': f'Token {token}'
}

data = {'address': '192.168.5.9/32'}
out = requests.post(f'{base_url}ipam/ip-addresses/', headers=http_headers, data=json.dumps(data), verify=False)
result = out.json()   
object_id = result['id']
addr = requests.get(f'{base_url}ipam/ip-addresses/{object_id}', headers=http_headers, verify=False)
pprint(addr.json())


# put request requires the 'address' field for some reason
desc = {'address': '192.168.5.9/32','description': 'some blurb'}
#desc = {'description': 'some blurb'}
change = requests.put(f'{base_url}ipam/ip-addresses/{object_id}/', headers=http_headers, verify=False, data=json.dumps(desc))

print()
pprint(change.json())

obj_del = requests.delete(f'{base_url}ipam/ip-addresses/{object_id}/', headers=http_headers, verify=False)

print()
print(obj_del.status_code)


