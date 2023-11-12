#!/usr/bin/python3
''' This module validates the Ip addresses'''
import re


def validate_ip_address(ip_address):
    pattern = r"\b(?:\b(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}\b(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b"
    match = re.match(pattern, ip_address)

    if match:
        return "Valid IP address"
    else:
        return "Invalid IP address"


# Testing the IP address regular expression
ip1 = "192.168.0.1"
ip2 = "10.0.0.255"
ip3 = "256.1.1.1"
ip4 = "abc.def.ghi.jkl"

print(validate_ip_address(ip1))
print(validate_ip_address(ip2))
print(validate_ip_address(ip3))
print(validate_ip_address(ip4))