# This function will show the data:

def show(jf): # Jason File as 'jf'
	print("+++++++++++++++++++++++++++++++++++++++++++++++++")
	print(f"+         Country : {jf['sys']['country']}          +")
	print("+++++++++++++++++++++++++++++++++++++++++++++++++")
	print(f"\tName...: {jf['name']}")
	print(f"\tId.....: {jf['id']}")
	# print(f"\tMain: {jf['main']}")
	print(f"\tTime Zone: {jf['timezone']}")
	print("Somenting wrong during show!")
