# FastMap

FastMap is a lightweight Python implementation that mimics some of the core functionalities of Nmap.

## Features
- Host discovery (ping / port reachability)
- TCP connect, SYN, and UDP scans
- Port status reporting (open/closed)
- Simple service detection via banner grabbing
- DNS A record resolution
- Export results to a plain text file
- Command line interface similar to Nmap

## Usage
```bash
python3 main.py -sT -p 22,80,443 192.168.1.0/24 -oN results.txt
```

## Dependencies
- Python 3.8+ (tested with 3.14)
- scapy
- dnspython

## Installation
```bash
pip install scapy dnspython
```

## Limitations
- Very basic OS fingerprinting.
- UDP scan results may be unreliable.
- Requires root for SYN scans.

## License
MIT
