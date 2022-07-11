import sys
import jinja2
import subprocess
templateLoader = jinja2.FileSystemLoader(searchpath='./')
templateEnv = jinja2.Environment(loader=templateLoader)
template_file = 'cisco3_config.j2'



config_deets = {'timezone': 'PST',
            'timezone_offset': '-8',
            'timezone_dst': 'PDT',
            'rd': '100:1',
            'ntp_1': '130.126.24.24',
            'ntp_2': '152.2.21.1',
            }




template = templateEnv.get_template(template_file)
output = template.render(config_deets=config_deets)

with open('rendered_config.txt', 'w') as f:
    f.write(output)


subprocess.run('diff ./cisco3-cfg.txt ./rendered_config.txt > ./diffs.txt', shell=True)

with open('./diffs.txt', 'r') as f:      
    diffs = f.read()

print('Differences:')
print('-' * 12)
print()
print(diffs)





