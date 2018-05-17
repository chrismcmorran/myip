#!/usr/bin/python
import sys
import urllib
import socket


def get_wan():
    ip_server = "https://nodejs-ipserver.herokuapp.com/"
    connection = urllib.urlopen(ip_server)
    wan = connection.read()
    return wan


def get_lan():
    host_name = socket.gethostname()
    lan = socket.gethostbyname(host_name)
    return lan


def print_usage():
    print('myip <flags>\n\t-l\tdisplay the local address\n\t-w\tdisplay the external address')


if len(sys.argv) == 1:
    print("WAN: {}".format(get_wan()))
    print("LAN: {}".format(get_lan()))
else:
    if '-l' in sys.argv:
        print("LAN: {}".format(get_lan()))
    if '-w' in sys.argv:
        print("WAN: {}".format(get_wan()))
    if '-h' in sys.argv:
        print_usage()