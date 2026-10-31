import dns.resolver


def resolve_a(host):
    """Resolve A records for host."""
    try:
        answers = dns.resolver.resolve(host, 'A')
        return [str(rdata) for rdata in answers]
    except Exception:
        return []


def resolve_ptr(ip):
    """Reverse DNS lookup for IP."""
    try:
        rev_name = dns.reversename.from_address(ip)
        answers = dns.resolver.resolve(rev_name, 'PTR')
        return [str(rdata).rstrip('.') for rdata in answers]
    except Exception:
        return []
