from netmiko import ConnectHandler

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": "p-word",
    "device_type": "cisco_nxos",
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": "p-word",
    "device_type": "cisco_nxos",
}

#for x in [nxos1, nxos2]:
#    net_connect = ConnectHandler(**x)
#    print(net_connect.find_prompt())



net_connect = ConnectHandler(**nxos1)
version = net_connect.send_command("show version")

#f = open("version.txt", "w")
#f.write(version)
#f.close

with open("version.txt", "w") as f:
    f.write(version)

net_connect.disconnect()

