Value NAME (\S+)
Value LINE_STATUS ((up|down))
Value ADMIN_STATE ((up|down))
Value MAC_ADDR ([a-f0-9]{4}\.[a-f0-9]{4}\.[a-f0-9]{4})
Value MTU (\d+)
Value DUPLEX ((full|half)-duplex)
Value SPEED (\d+)



Start
  ^${NAME} is ${LINE_STATUS}$$
  ^admin state is ${ADMIN_STATE},
  ^  Hardware:.*address: ${MAC_ADDR}\s
  ^  MTU ${MTU} bytes
  ^  ${DUPLEX}, ${SPEED} Mb/s -> Record

EOF


#Ethernet2/1 is up
#admin state is up, Dedicated Interface
#  Hardware:  Ethernet, address: 000c.29d1.d56b (bia 2cc2.605e.5dba)
#  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec
#  reliability 255/255, txload 1/255, rxload 1/255
#  Encapsulation ARPA, medium is broadcast
#  Port mode is routed
#  full-duplex, 1000 Mb/s
#  Beacon is turned off
#  Auto-Negotiation is turned off


