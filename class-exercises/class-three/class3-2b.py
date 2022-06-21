from pprint import pprint
import yaml

with open('device_list.yml', 'r') as f:
    device_list = yaml.safe_load(f)

pprint(device_list)
