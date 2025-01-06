"""

Write a Python program to access and print the html contents of a URL to the console.

Hint: use the built-in 'http' module or the 'requests' module

Host: https://www.w3resource.com/python-exercises/python-basic-exercise-101.php

"""

# a package that collects several modules for working with the HyperText Transfer Protocol
# http.client is a low-level HTTP protocol client; for high-level URL opening use urllib.request
# This module defines classes that implement the client side of the HTTP and HTTPS protocols.
# HTTPConnection An HTTPConnection instance represents one transaction with an HTTP server.
# HTTPSConnection A subclass of HTTPConnection that uses SSL for communication with secure servers
from http.client import HTTPSConnection

# an elegant and simple HTTP library for Python, built for human beings.
import requests


def main():
    # Create an HTTPConnection object for the target host.
    conn = HTTPSConnection("www.w3resource.com")  # no 'https://' on the front (the 'http' is considering ':'
    # as a port number and the port number must be numeric)

    # send a request to the server using the HTTPs request method "Get" and the request URI
    # /python-exercises/python-basic-exercise-101.php.
    conn.request("GET", "/python-exercises/python-basic-exercise-101.php")

    # called after a request is sent to get the response from the server. Returns an HTTPResponse instance.
    res = conn.getresponse()

    # Reads and returns the response body, or up to the next amt bytes.
    html = res.read()

    print(html)

    print("=" * 25)

    # Send an HTTP GET request to a URL and store the response.
    data = requests.get("https://www.w3resource.com/python-exercises/python-basic-exercise-101.php")

    # Access the text content of the response, which contains the webpage's HTML.
    html = data.text

    # Print the HTML content of the webpage.
    print(html)


if __name__ == "__main__":
    main()
