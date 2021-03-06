#!/usr/bin/env python
import getpass
import telnetlib

#Username and password
HOST = '192.168.1.1'
user = input('Enter your username: \n")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"terminal length 0\n")
tn.write(b"show version\n")
tn.write(b"exit\n")

str1 = (tn.read_all().decode('ascii'))
int1 = (str1.index('Version'))
print(str1[int1: int1 + 21])
