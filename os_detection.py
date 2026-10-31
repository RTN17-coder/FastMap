import socket
import re

# Very simple OS fingerprinting based on banner and common port patterns

def fingerprint_os(host, ports, service_map):
    # Heuristic: if 22 is open and banner contains 'Linux', assume Linux
    os_name = 'unknown'
    if 22 in ports and ports[22]['open']:
        banner = service_map.get(22)
        if banner and 'Linux' in banner:
            os_name = 'Linux'
    if os_name == 'unknown':
        # check for Windows banner on SMB port 445
        if 445 in ports and ports[445]['open']:
            banner = service_map.get(445)
            if banner and 'Windows' in banner:
                os_name = 'Windows'
    return os_name
