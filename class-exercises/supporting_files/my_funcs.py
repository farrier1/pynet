import yaml

def read_yaml(file):
    with open(file, 'r') as f:
        sw_deets = yaml.safe_load(f)
    return sw_deets

def print_arp(arp_entry):
    for n in arp_entry:
        print('IP Address: {address} HW Address: {hwAddress}'.format(**n))   
    return

