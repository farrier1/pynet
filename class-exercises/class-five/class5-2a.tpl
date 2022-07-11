interface Ethernet1/1
 ip address {{ ip }}/{{ mask}}
 
router bgp {{ as }}
 neighbor {{ peer_ip }} remote-as {{ as }}
 address-family ipv4 unicast
