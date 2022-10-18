#!/usr/bin/env python3
import scapy.all as scapy

def scan(ip):           
    arp_request= scapy.ARP()
    arp_request.pdst=ip                 # setting for which ip has to searched
    print(arp_request.summary())
    #scapy.ls(scapy.ARP())            #show the names of variables that we can show to set in ARP() class

scan("10.0.0.0")
