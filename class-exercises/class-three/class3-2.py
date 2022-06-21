import re
from pprint import pprint

#f.seek(0, 0)


def create_list(f):
    line = '1'
    dict = {}
    devices = []
    while line != '\n':
        line = f.readline()
        line_str = list(line.split())
        if 'hostname' in line_str:
            dict = {'device_name': line_str[2]}
        elif 'username' in line_str:
            dict = {'username': line_str[2]}
        elif 'password' in line_str:
            dict = {'password': line_str[2]}
        else:
             continue
        devices.append(dict)
    return devices

f = open('./router_data.txt', 'r')
devices = create_list(f)
pprint(devices)









#    host = line_str[2].split('.')[0]

