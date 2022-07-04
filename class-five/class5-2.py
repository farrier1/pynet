import jinja2
templateLoader = jinja2.FileSystemLoader(searchpath='./')
templateEnv = jinja2.Environment(loader=templateLoader)
template_file = 'class5-2.tpl'


nxos1 = {
    'ip': '10.1.100.1',
    'mask': '24',
}   

nxos2 = {
    'ip': '10.1.100.2',
    'mask': '24',
}

devices = [nxos1, nxos2]

for device in devices:
#for device in (nxos1, nxos2):
    template = templateEnv.get_template(template_file)
    output = template.render(**device)
    print(output)




