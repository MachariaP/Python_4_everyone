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

server_addr = input("What server do you want to connect to? ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
