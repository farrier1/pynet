from jinja2 import Template

bgp_deets = {
    'local_as': '10',
    'peer1_ip': '10.1.20.2',
    'peer1_as': '20',
    'peer2_ip': '10.1.20.2',
    'peer2_as': '20',
}   

bgp_template = '''
router bgp {{ local_as }}
  neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor {{ peer2_ip }} remote-as {{ peer_2_as }}
    address-family ipv4 unicast
'''

template = Template(bgp_template)
output = template.render(bgp_deets)

print(output)

# router bgp 10
#  neighbor 10.1.20.2 remote-as 20
#    update-source loopback99
#    ebgp-multihop 2
#    address-family ipv4 unicast
#  neighbor 10.1.30.2 remote-as 30
#    address-family ipv4 unicast

