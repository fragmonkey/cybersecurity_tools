#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('cls', shell=True)
openPorts=""

#input
remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)
portStartRange = input("Enter Port Starting Range: ")
portEndRange = input("Enter Port Ending Range: ")

print ("-" * 60)
print ("Scanning Please Wait...", remoteServerIP)
print ("-" * 60)


try:
	print ("Scanning IP:",remoteServerIP," with port range: ",int(portStartRange), " through ",int(portEndRange))
	for port in range(int(portStartRange),int(portEndRange)):
		#print("Checking Port",format(port))
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print ("Port {}:  Open".format(port))
			openPorts = format(port)
		sock.close()
	print("All Open Ports: ",openPorts)

except KeyboardInterrupt:
	print ("You pressed CTRL+C")
	sys.exit()

except socket.gaierror:
	print("Could not connect to server")
	sys.exit()

except socket.error:
	print("Could not connect to server")
	sys.exit()