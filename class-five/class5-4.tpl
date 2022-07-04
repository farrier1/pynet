{% for element in bgp_deets %}
    vrf definition {{ element.vrf_name }}
     rd {{ element.rd }}
    {%-if element.ipv4 %}
     !
     address-family ipv4
      route-target export 100:1
      route-target import 100:1
     exit-address-family
    {%-endif %}
    {%-if element.ipv6 %}
     !
     address-family ipv6
      route-target export 100:1
      route-target import 100:1
     exit-address-family
    {%-endif %}
{% endfor %}
