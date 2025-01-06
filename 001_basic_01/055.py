"""

Write a Python program to find local IP addresses using Python's stdlib.

"""

# Import the 'socket' module to work with network-related functions.
# On top of the operating system, the socket module defines how servers and clients communicate at hardware level.
# In addition to supporting connection-oriented protocols, the socket API also supports connectionless protocols.
import socket


def main():
    # Step 1: Get the local hostname.
    local_hostname = socket.gethostname()

    print(f"Local hostname: {local_hostname}")

    # Step 2: Get a list of IP addresses associated with the hostname.
    # translate a host name to IPv4 address format, extended interface.
    # Return a triple (hostname, aliaslist, ipaddrlist) where hostname is the host’s primary host name.
    _, _, ip_addr_list = socket.gethostbyname_ex(local_hostname)

    # Step 3: Filter out loopback addresses (IPs starting with "127.") (reserved for loopback testing).
    filtered_ips = [ip for ip in ip_addr_list if not ip.startswith("127.")]

    # Step 4: Extract the first IP address (if available) from the filtered list.
    first_ip = filtered_ips[0]

    print(f"Your IP address: {first_ip}")


if __name__ == "__main__":
    main()
