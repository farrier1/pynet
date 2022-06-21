import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse


# set peers empty list
peers = []

# pull in BGP config
parsed = CiscoConfParse('./bgp_config.txt', factory=True)

# find neighbors that have a remore-as set
neighbors = parsed.find_objects_w_child(parentspec=r'neighbor', childspec=r'remote-as')

# iteraret through neighbours, find IP
for n in neighbors:
    ip = (n.text.split()[1])
# Iterate through children to find remote-as
    for r in n.children:
        if r.text.split()[0] == 'remote-as':
            remote_as = (r.text.split()[1])
# add to peer tuple
            peer = (ip, remote_as)
# add peer tunple to peers list
            peers.append(peer)

        
print(peers)







