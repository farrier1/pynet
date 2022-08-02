import xmltodict
from pprint import pprint

def parse_xml(filename, force_flag):
    xml_file = open(filename)
    xml_data = xml_file.read().strip()
    if force_flag == True:
        my_xml = xmltodict.parse(xml_data, force_list={'zones-security': True})
    else:
        my_xml = xmltodict.parse(xml_data)
    return my_xml


if __name__ == '__main__':
    zones = parse_xml('show_security_zones.xml', 0)
    zone = parse_xml('show_security_zones_single_trust.xml', 0)

    print('Zones:', type(zones['zones-information']['zones-security']))
    print()
    pprint(zones)
    print
    print('Zone:', type(zone['zones-information']['zones-security']))
    pprint(zone)
    print
    print('Types are different as \'zones\' has multiple \'zones-security\' so puts them in a list')
    print()
    print('Now with \'force_list\ flag:')
    print()    
    zones = parse_xml('show_security_zones.xml', 1)
    zone = parse_xml('show_security_zones_single_trust.xml', 1)
    print('Zones:', type(zones['zones-information']['zones-security']))
    print()
    pprint(zones)
    print
    print('Zone:', type(zone['zones-information']['zones-security']))
    pprint(zone)
    print()
    print('Note both types are now a list') 
    
