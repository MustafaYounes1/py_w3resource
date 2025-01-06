"""

Write a Python program to get the domain name using PTR DNS records from a given IP address.

What is a DNS PTR record?

The Domain Name System, or DNS, correlates domain names with IP addresses. A DNS pointer record (PTR for short) provides
 the domain name associated with an IP address. A DNS PTR record is exactly the opposite of the 'A' record, which
 provides the IP address associated with a domain name.

DNS PTR records are used in reverse DNS lookups. When a user attempts to reach a domain name in their browser, a DNS
lookup occurs, matching the domain name to the IP address. A reverse DNS lookup is the opposite of this process: it is
a query that starts with the IP address and looks up the domain name. Source: cloudflare.com

print(get_domain_name("8.8.8.8"))           =>  dns.google
print(get_domain_name("13.251.106.90"))     =>  ec2-13-251-106-90.ap-southeast-1.compute.amazonaws.com
print(get_domain_name("8.8.4.4"))           =>  dns.google
print(get_domain_name("23.23.212.126"))     =>ec2-23-23-212-126.compute-1.amazonaws.com

"""

import socket


__ips = [
    "8.8.8.8",
    "13.251.106.90",
    "8.8.4.4",
    "23.23.212.126",
]


def main():
    for ip in __ips:
        print(socket.gethostbyaddr(ip)[0])


if __name__ == "__main__":
    main()
