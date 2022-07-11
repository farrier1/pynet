import jinja2
from netmiko import ConnectHandler
from my_devices import nxos1, nxos2

templateLoader = jinja2.FileSystemLoader(searchpath='./')
templateEnv = jinja2.Environment(loader=templateLoader)
template_file = 'class5-2a.tpl'


devices = [
     {
        'host': 'nxos1',
        'ip': '10.1.100.1',
        'mask': '24',
        'as': '22',
        'peer_ip': '10.1.100.2',
    }, 
    {
        'host': 'nxos2',
        'ip': '10.1.100.2',
        'mask': '24',
        'as': '22',
        'peer_ip': '10.1.100.1',
    }
]

hosts = [nxos1, nxos2]

for n, host in enumerate(hosts):
    template = templateEnv.get_template(template_file)
    output = template.render(**devices[n])
    commands = output.splitlines()
    ssh = ConnectHandler(**host)
    ssh.send_config_set(commands)
    
for n, host in enumerate(hosts):    
    result = ssh.send_command('ping ' + devices[n]['peer_ip'])
    if '0.00% packet loss' in result:
        print('Neighbour', devices[n]['peer_ip'], 'is alive!')
    else:
        print(devices[n]['peer_ip'], 'is dead Jim, dead.')

for device in hosts:
    ssh.disconnect()

'''
BGP check config below from pynet site

 for device in (nxos1,):
        net_connect = device["ssh_conn"]
        remote_ip = device["j2_vars"]["peer_ip"]

        # Test ping
        output = net_connect.send_command(f"ping {remote_ip}")
        print(output)
        if "64 bytes from" not in output:
            print("\nPing failed!!!")
        print("\n\n")

        # Test BGP
        bgp_verify = f"show ip bgp summary | include {remote_ip}"
        output = net_connect.send_command(bgp_verify)
        # Retrieve the State/PfxRcd field which is the last field
        match = re.search(r"\s+(\S+)\s*$", output)
        prefix_received = match.group(1)
        try:
            # If this is an integer, the BGP session reached the established state
            int(prefix_received)
            print(
                f"BGP reached the established state. Prefixes received {prefix_received}"
            )
        except ValueError:
            print("BGP failed to reach the established state")
'''























