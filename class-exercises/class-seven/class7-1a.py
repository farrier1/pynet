from lxml import etree

with open('show_security_zones.xml') as f:
    my_xml = f.read()


my_xml = etree.fromstring(my_xml)

print(my_xml)
print(type(my_xml))
print()
print()
print()

my_xml_str = etree.tostring(my_xml).decode()
print(my_xml_str)

my_xml.tag
my_xml.getchildren()
print(my_xml.tag)
child_element_len = len(my_xml.getchildren())
print('1c: No. of child elements:', child_element_len)
first_tag = my_xml.getchildren()[0].tag
print('1d: 1st child element name:', first_tag)


trust_zone = my_xml.getchildren()[0]
print(trust_zone.getchildren())
print()
trust_zone = trust_zone.getchildren()
print('1f: Child element tags of Trust Zone')
for i, t in enumerate(trust_zone):
    print(trust_zone[i].tag)





