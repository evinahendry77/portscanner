#!/bin/python
import sys
import socket
from datetime import datetime

# Define the target.
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid number of arguments.")
	print("Syntax: 'python3 scanner.py <ip>'")

print("-" * 75)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

# Scan.
try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0:
			print("Port {} is open.".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nKeyboard interruption detected. Exiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to the server.")
	sys.exit()
