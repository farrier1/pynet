import textfsm
from pprint import pprint

data_list = []

template_file = './class4-2.tpl'
template = open(template_file)

with open('./show_int.txt') as f:
    raw_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_data)

template.close()

for i in data:
    data_dict = {'DUPLEX': i[4],
                'PORT_NAME': i[0],
                'PORT_TYPE': i[5],
                'SPEED': i[4],
                'STATUS': i[1],
                'VLAN': i[2]}
    data_list.append(data_dict)

pprint(data_list)

print(re_table.header)
                  
'''
DS Solution for list to dict below:

table_keys = re_table.header
final_list = []
for fsm_list in data:
    fsm_dict = dict(zip(table_keys, fsm_list))
    final_list.append(fsm_dict) 
'''


#class4-2.tpl
#show_int.txt
