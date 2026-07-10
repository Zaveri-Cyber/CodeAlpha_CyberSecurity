from scapy.all import *

def packet_info(packet):
    if packet.haslayer(IP):
        print("\n===== Packet Captured =====")
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)
        print("Protocol       :", packet[IP].proto)

sniff(prn=packet_info, store=False)
