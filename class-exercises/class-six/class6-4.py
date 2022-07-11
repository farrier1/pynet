from pprint import pprint
import pyeapi
from getpass import getpass
import jinja2
import yaml
from my_funcs import read_yaml
templateLoader = jinja2.FileSystemLoader(searchpath='./')
templateEnv = jinja2.Environment(loader=templateLoader)
template_file = 'class6-4.tpl'

sw_deets = read_yaml('./aristas.yaml')
passwd = getpass()

for k in sw_deets:
    config_deets = sw_deets[k]['data']
    template = templateEnv.get_template(template_file)
    cfg = template.render(config_deets=config_deets)
    cfg = cfg.split('\n')
    connection = pyeapi.client.connect(**sw_deets[k], password=passwd)
    device = pyeapi.client.Node(connection)
    output =  device.config(cfg)
    output = device.enable('show ip interface brief')
    print('=' * 28)
    print(k, 'IP interface details')
    pprint(output[0]['result']['output'])
    print('=' * 28 )

