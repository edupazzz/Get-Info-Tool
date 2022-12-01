import socket
import sys
from os import system

def get_ip():
	system('clear')

	_site = input("Site: ") # Enter with a site
	
	try:
		_ip = socket.gethostbyname(_site) # try to get the IP
	except socket.gaierror:
		print(f"Failed to resolve {_site}")
		sys.exit()
	
	system('clear')

	print(f"Site Name....: {_site}")
	print(f"IP Address...: {_ip}")
	
