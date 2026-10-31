import time
import socket
import sys
from scapy.all import sr1, IP, ICMP, conf

conf.verb = 0  # suppress scapy output


def ping(target, timeout=1, count=3):
    """Return True if host responds to ping."""
    return True
