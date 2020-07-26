# lolpinger
A small programm to check your ping to the LOL EUW server

use the programm with "sudo python3 ping.py" from command line

sudo is required because apparently pythonping uses ICMP which creates raw IP packets and sniff the traffic on the network card. OS are designed to require root rights for these operations by design
