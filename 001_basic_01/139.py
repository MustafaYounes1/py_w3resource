"""

Write a Python program to validate an IP address.

An Internet Protocol address (IP address) is a numerical label assigned to each device connected to a computer
network that uses the Internet Protocol for communication. An IP address serves two main functions: host or network
interface identification and location addressing.

Internet Protocol version 4 (IPv4) defines an IP address as a 32-bit number. However, because of the growth of the
Internet and the depletion of available IPv4 addresses, a new version of IP (IPv6), using 128 bits for the IP address,
was standardized in 1998. IPv6 deployment has been ongoing since the mid-2000s.

IP addresses are written and displayed in human-readable notations, such as 172.16.254.1 in IPv4, and
2001:db8:0:1234:0:567:8:1 in IPv6. The size of the routing prefix of the address is designated in CIDR notation
by suffixing the address with the number of significant bits, e.g., 192.168.1.15/24, which is equivalent to the
historically used subnet mask 255.255.255.0.

     10.0.0.0 -> Valid Ip address

     10.255.255.255 -> Valid Ip address

     192.168.255.0 -> Valid Ip address

     266.1.0.2 -> Invalid Ip address

"""

import socket


def main():
    for add in [
        "10.0.0.0",
        "10.255.255.255",
        "192.168.255.0",
        "266.1.0.2",
    ]:
        try:
            # Convert an IPv4 address from dotted-quad string format (for example, ‘123.45.67.89’) to 32-bit packed
            # binary format, as a bytes object four characters in length.
            _ = socket.inet_aton(add)
            print(f"{add.ljust(25)} is valid")

        except socket.error:
            print(f"{add.ljust(25)} is invalid")


if __name__ == "__main__":
    main()
