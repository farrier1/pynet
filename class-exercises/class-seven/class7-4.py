from lxml import etree

with open('show_security_zones.xml') as f:
    my_xml = f.read()


my_xml = etree.fromstring(my_xml)

my_xml_e1 = my_xml.find('.//zones-security')

print('4a: Tag of first zone-sec element')
print(my_xml_e1.tag)
print()
print('4a: Tags of all child elements of above')
for i, e in enumerate(my_xml_e1):
    print(my_xml_e1[i].tag)

print()
print('4b: First sec zonename')
print(my_xml.find('.//zones-security-zonename').text)
print()


print('4c: Sec zone names')
sec_zones = my_xml.findall('zones-security')
for i, e in enumerate(sec_zones):
    print(sec_zones[i].find('zones-security-zonename').text)









