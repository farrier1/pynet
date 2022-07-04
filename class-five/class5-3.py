import sys
import jinja2
templateLoader = jinja2.FileSystemLoader(searchpath='./')
templateEnv = jinja2.Environment(loader=templateLoader)
template_file = 'class5-3.tpl'

ipv4 = eval(sys.argv[1])
ipv6 = eval(sys.argv[2])



bgp_deets = {'ipv4': ipv4, 'ipv6': ipv6, 'vrf_name': 'blue', 'rd': '100:1'}


template = templateEnv.get_template(template_file)
output = template.render(**bgp_deets)
print(output)





