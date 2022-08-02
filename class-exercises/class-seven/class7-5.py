from lxml import etree

with open('show_version.xml', 'rb') as f:
    my_xml = f.read()


my_xml = etree.fromstring(my_xml)
print()
print('5a: Namespaces')
print(my_xml.nsmap)

serial = my_xml.find('.//{*}proc_board_id').text
print()
print('5b: Serial Number')
print(serial)









