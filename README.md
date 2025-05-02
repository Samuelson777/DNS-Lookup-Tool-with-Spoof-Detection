# DNS Lookup Tool with Spoof Detection

## Overview
This DNS Lookup Tool with Spoof Detection is a Python script that performs DNS lookups for a given domain using multiple public DNS resolvers (Google DNS, Cloudflare, OpenDNS, Quad9). It compares the resolved IP addresses to detect potential DNS spoofing or poisoning by identifying inconsistencies in DNS responses.

This tool enhances understanding of DNS behavior and provides a practical method to check DNS security risks related to spoofing.

## Features
- Query multiple public DNS servers for A records of a domain.
- Compare the IP addresses returned by each server.
- Detect inconsistencies that may indicate DNS spoofing or poisoning.
- User-friendly command-line interface with error handling.

## Usage
1. Ensure you have Python installed.
2. Install the required `dnspython` library if not already installed:
3. Run the script
4. Enter the domain name to query when prompted (do NOT include `http://` or `https://`).

## Example Screenshot

![DNS Lookup Tool with Spoof Detection](https://github.com/user-attachments/assets/49bcfc6b-59e6-409e-8176-f5c294355397)

## Conclusion  
This DNS Lookup Tool with Spoof Detection provides a simple yet effective way to verify DNS responses from multiple public DNS resolvers. By comparing the returned IP addresses from different servers, the tool helps detect potential DNS spoofing or poisoning attacks, enhancing awareness and security in network communications. It serves as a practical educational tool for understanding DNS behavior and the importance of DNS security.

## Restriction Warning  
This tool is intended solely for educational and authorized testing purposes. Performing DNS queries on domains without permission or using the tool to disrupt services or launch attacks is unethical and may be illegal. Always ensure you have explicit permission before probing any domain or network. Misuse of this tool can have legal consequences.

## Future Enhancements  
- Support additional DNS record types such as AAAA (IPv6), MX (mail servers), and TXT records for SPF/DKIM verification.  
- Add the ability to query customizable DNS servers specified by the user.  
- Implement parallel querying to speed up lookups from multiple servers.  
- Incorporate geo-IP lookup to analyze the physical locations of resolved IP addresses.  
- Provide more detailed reporting with timestamps and export options (e.g., CSV, JSON).  
- Enhance spoof detection with heuristic analysis or integration with threat intelligence feeds.  
- Build a graphical user interface (GUI) for easier operation by non-technical users.

## License  
This project is open source and available under the MIT License.
