#!/usr/bin/env python
import netfilterqueue


def process_packet(packet):
    packet.drop()
    print("[+] Packet Dropped.")


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
