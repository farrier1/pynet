import xmltodict


xml_file = open('show_security_zones.xml')

xml_data = xml_file.read().strip()

my_xml = xmltodict.parse(xml_data)

print('2a:')
print(my_xml)
print()

print('2b')
sec_zone = my_xml['zones-information']['zones-security']
for i, z in enumerate(sec_zone):
    print('Security Zone #{}: {}'.format(i, sec_zone[i]['zones-security-zonename']))



