import sys
import time

def slow_p(_txt):
	for c in _txt: # slowly print the output
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1)

