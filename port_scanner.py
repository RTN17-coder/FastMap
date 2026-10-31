import socket
import time
from scapy.all import IP, TCP, UDP, sr1, conf

conf.verb = 0

def tcp_connect_scan(host, port, timeout=1):
    """Return True if TCP port is open via connect."""
    try:
        s = socket.create_connection((host, port), timeout=timeout)
        s.close()
        return True
    except Exception:
        return False


def tcp_syn_scan(host, port, timeout=1):
    """Return True if TCP port is open via SYN scan (requires root)."""
    pkt = IP(dst=host)/TCP(dport=port, flags='S')
    resp = sr1(pkt, timeout=timeout, verbose=0)
    if resp and resp.haslayer(TCP) and resp.getlayer(TCP).flags == 0x12:  # SYN+ACK
        # send RST to close
        sr1(IP(dst=host)/TCP(dport=port, flags='R'), timeout=timeout, verbose=0)
        return True
    return False


def udp_scan(host, port, timeout=1):
    """Return True if UDP port is open. Very unreliable."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(timeout)
        s.sendto(b'', (host, port))
        try:
            data, _ = s.recvfrom(1024)
            s.close()
            return True
        except socket.timeout:
            s.close()
            return False
    except Exception:
        return False


def scan_ports(host, ports, scan_type='connect', timeout=1):
    results = {}
    for port in ports:
        if scan_type == 'connect':
            open_ = tcp_connect_scan(host, port, timeout)
        elif scan_type == 'syn':
            open_ = tcp_syn_scan(host, port, timeout)
        elif scan_type == 'udp':
            open_ = udp_scan(host, port, timeout)
        else:
            open_ = False
        results[port] = open_
    return results
