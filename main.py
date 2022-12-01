""" The Main Code """
from slow_print import slow_p
from gip_address import get_ip
from glocation import get_location
import time 
import sys
from os import system
from choose_function import getFunction
###########################################################################
# Txt session:
intro_txt = "Hello!\nCongratulations, you have access to an\nexperimental program...  .... .."
choose_txt = "You need to choose a tool:\n"
###########################################################################
# Print Intro 
#slow_p(intro_txt)
slow_p(choose_txt)
###########################################################################
# Start the main loop
while(1): 
	getFunction()
