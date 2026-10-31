import argparse


def build_parser():
    parser = argparse.ArgumentParser(description='Mini Nmap - Network scanner')
    parser.add_argument('-sT', action='store_true', help='TCP connect scan (default)')
    parser.add_argument('-sS', action='store_true', help='TCP SYN scan')
    parser.add_argument('-sU', action='store_true', help='UDP scan')
    parser.add_argument('-p', default='1-1024', help='Port range (e.g., 22,80,443 or 1-65535)')
    parser.add_argument('-oN', metavar='FILE', help='Output to normal file')
    parser.add_argument('targets', nargs='+', help='Target host(s) or CIDR block')
    return parser
