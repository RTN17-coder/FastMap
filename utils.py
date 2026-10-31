import ipaddress


def parse_ports(port_str):
    """Parse port string like '22,80,443' or '1-1024' into list of ints"""
    ports = set()
    for part in port_str.split(','):
        if '-' in part:
            start, end = part.split('-', 1)
            ports.update(range(int(start), int(end)+1))
        else:
            ports.add(int(part))
    return sorted(ports)


def expand_targets(targets):
    """Return target list as provided, without expanding CIDR blocks."""
    return list(targets)
