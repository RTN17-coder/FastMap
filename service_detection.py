import socket
import time
import re
from typing import Optional

# Simple banner grabber with timeout

def grab_banner(host: str, port: int, timeout=2) -> Optional[str]:
    """Attempt to connect and read up to 1024 bytes for banner."""
    try:
        with socket.create_connection((host, port), timeout=timeout) as s:
            s.settimeout(timeout)
            try:
                data = s.recv(1024)
                return data.decode(errors='ignore').strip()
            except socket.timeout:
                return None
    except Exception:
        return None

# Detect service based on common ports and banner heuristics
PORT_SERVICE_MAP = {
    80: 'http',
    443: 'https',
    22: 'ssh',
    21: 'ftp',
    25: 'smtp',
    110: 'pop3',
    143: 'imap',
    53: 'dns',
    3306: 'mysql',
    5432: 'postgres',
    1521: 'oracle',
    3389: 'rdp',
}

def detect_service(host: str, port: int) -> str:
    """Return service name or banner. Simple heuristic."""
    if port in PORT_SERVICE_MAP:
        return PORT_SERVICE_MAP[port]
    banner = grab_banner(host, port, timeout=2)
    if banner:
        # simple regex for common services
        if re.search(r"(?i)ssh", banner):
            return "ssh"
        if re.search(r"(?i)ftp", banner):
            return "ftp"
        if re.search(r"(?i)http", banner):
            return "http"
        if re.search(r"(?i)smtp", banner):
            return "smtp"
        return banner.split()[0]
    return "unknown"
