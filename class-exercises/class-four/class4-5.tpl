Value DEVICE (\S+)
Value LOCAL_INT (\S+)
Value CAPABILITY (\S+)
Value PORT (\S+)



Start
  ^Device.*Port ID\s* -> Lldp

Lldp
  ^${DEVICE}\s+${LOCAL_INT}\s+\d+\s+${CAPABILITY}\s+${PORT} -> Record
  


EOF

#Capability codes:
#  (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
#  (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
#Device ID                         Local Intf          Hold-time   Capability  Port ID     
#nxos2.twb-tech.com                Eth2/1              120          BR          Eth2/1      
#nxos2.twb-tech.com                Eth2/2              120          BR          Eth2/2      
#nxos2.twb-tech.com                Eth2/3              120          BR          Eth2/3      
#nxos2.twb-tech.com                Eth2/4              120          BR          Eth2/4      
#Total entries displayed: 4

