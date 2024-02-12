from os import system
from sys import exit
from slow_print import slow_p
from gip_address import get_ip
from glocation import get_location
###########################################################################
wellDone_txt = "\nWell Done!\n What do you want to do now?\n"
showOp = "[1] Get IP\n[2] Get Location\n[0] Quit\n"


def getFunction():
	print(showOp)
	try:
		uc = int(input(">>> "))
	except:
		print("Numbers Only!\n")
	if uc == 0:
		exit()
	elif uc == 1:
		get_ip()
	elif uc == 2:
		get_location()
	else:
		system('clear')
		print("Not Avaliable!\n")
###########################################################################
# After the function call 
	slow_p(wellDone_txt)
