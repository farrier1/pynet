import subprocess

device2 = subprocess.run('curl -L -s -H "Authorization: Token $NETBOX_TOKEN" https://netbox.lasthop.io/api/dcim/devices/2 --insecure | jq', shell=True)


print(device2)
