vrf definition {{ vrf_name }}
 rd {{ rd }}
 !
{%-if ipv4 %}
 address-family ipv4
  route-target export 100:1
  route-target import 100:1
 exit-address-family
{%-endif %}
 !
{%-if ipv6 %}
 address-family ipv6
  route-target export 100:1
  route-target import 100:1
 exit-address-family
{%-endif %}
