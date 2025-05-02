"""
DNS Lookup Tool with Spoof Detection

This script performs DNS lookups for a given domain using multiple public DNS resolvers.
It compares the results to detect potential DNS spoofing or poisoning by checking for inconsistent responses.

Usage:
    python dns_lookup_spoof_detection.py
"""

import dns.resolver

# List of public DNS servers to query
DNS_SERVERS = {
    "Google DNS": "8.8.8.8",
    "Cloudflare DNS": "1.1.1.1",
    "OpenDNS": "208.67.222.222",
    "Quad9": "9.9.9.9"
}


def query_dns(domain, server_ip):
    """
    Query the DNS server for A records of the domain.
    Return set of IP addresses as strings or None on failure.
    """
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [server_ip]
    try:
        answers = resolver.resolve(domain, 'A', lifetime=5)
        ips = {answer.to_text() for answer in answers}
        return ips
    except dns.exception.DNSException as e:
        print(f"Error querying {server_ip}: {e}")
        return None


def detect_spoofing(results):
    """
    Analyze the results from multiple DNS servers.
    Return True if inconsistencies detected, else False.
    """
    # Filter out None results
    valid_results = [ips for ips in results.values() if ips is not None]

    if not valid_results:
        return False  # No valid results to compare

    # Use the first valid result as the baseline
    baseline = valid_results[0]

    # Check if any other result differs
    for ips in valid_results[1:]:
        if ips != baseline:
            return True
    return False


def main():
    print("=== DNS Lookup Tool with Spoof Detection ===")
    domain = input("Enter the domain name to query (e.g. example.com): ").strip()
    
    # Remove any protocol from the input
    if domain.startswith("http://"):
        domain = domain[7:]
    elif domain.startswith("https://"):
        domain = domain[8:]

    if not domain:
        print("No domain entered. Exiting.")
        return

    print(f"\nQuerying DNS servers for domain: {domain}\n")

    results = {}
    for name, server_ip in DNS_SERVERS.items():
        ips = query_dns(domain, server_ip)
        if ips is None:
            print(f"{name} ({server_ip}): Query failed or timed out.")
        else:
            print(f"{name} ({server_ip}): {', '.join(sorted(ips))}")
        results[name] = ips

    print("\nAnalyzing results for DNS spoofing detection...")
    spoofing_detected = detect_spoofing(results)

    if spoofing_detected:
        print("WARNING: DNS spoofing or poisoning detected! Different DNS servers returned different results.")
    else:
        print("No DNS spoofing detected. All servers returned consistent results.")

    print("\nTool completed.")


if __name__ == "__main__":
    main()
