#!/usr/bin/env python3

"""
We want to write a program which reads the address of a WWW site using the
standard input() function and fetches the root document of the specified site.

Our program will perform the following steps:
    1. Create a new socket: able to handle connection-oriented transmissions
            based on TCP.

    2. Connect the socket to the HTTP server of a given address.

    3. Send a request to the server (the server want to know what we want from it).

    4. Receive the server's response (It will contain the requested root
       document of the site).

    5. Close the socket (End the connection)
"""
import socket

# Get server address
server_addr = input("What server do you want to connect to? ")

# Create a TCP socket for INET domain
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server on port 80 (HTTP)
sock.connect((server_addr, 80))

# Send HTTP GET request
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")
