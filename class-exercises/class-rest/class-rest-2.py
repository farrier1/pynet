import requests
from pprint import pprint


base_url = 'https://netbox.lasthop.io/api/'

#out = requests.get('https://netbox.lasthop.io/api/', verify=False)

http_headers = {}
http_headers['accept'] = 'application/json; version=2.4;'

out = requests.get(base_url, headers=http_headers, verify=False)


print('=' * 36)
print(f'Status Code:\n{out.status_code}')
print('=' * 36)
print(f'Text:\n{out.text}')
print('=' * 36)
print(f'JSON:\n{out.json()}')
print('=' * 36)
print(f'Headers:\n{out.headers}')
print('=' * 36)

