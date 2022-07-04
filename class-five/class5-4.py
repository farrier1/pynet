import sys
import jinja2
templateLoader = jinja2.FileSystemLoader(searchpath='./')
templateEnv = jinja2.Environment(loader=templateLoader)
template_file = 'class5-4.tpl'



bgp_deets = [{'ipv4': True, 'ipv6': True, 'vrf_name': 'blue', 'rd': '100:1'},
            {'ipv4': False, 'ipv6': True, 'vrf_name': 'red', 'rd': '100:1'},
            {'ipv4': True, 'ipv6': True, 'vrf_name': 'yellow', 'rd': '100:1'},
            {'ipv4': False, 'ipv6': False, 'vrf_name': 'green', 'rd': '100:1'},
            {'ipv4': True, 'ipv6': True, 'vrf_name': 'mauve', 'rd': '100:1'}]




template = templateEnv.get_template(template_file)
output = template.render(bgp_deets=bgp_deets)
print(output)





