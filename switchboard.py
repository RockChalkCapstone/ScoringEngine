#!/usr/bin/python3

import backend
from sys import argv

def main():
	#load variables and run function.
	if(len(argv) <= 1):
		print("---------------------------------------------------------------")
		print("-                        Overview:                            -")
		print("---------------------------------------------------------------")
		print("            From the terminal run this script.                 ")
		print("Include the function you would like to run without paranthesis.")
		print("           Followed by your variables in order.                ")
		print("Format: python switchboard.py <function> <var1>, <var2>, etc...")
		exit(1)
	elif(len(argv) == 2):
		function_name = argv[1]
		print("Running function: " + function_name +"()")
	elif(len(argv) == 3):
		function_name = argv[1]
		var1 = argv[2]
		print("Running function: " + function_name +"("+ var1 +")")
	elif(len(argv) == 4):
		function_name = argv[1]
		var1 = argv[2]
		var2 = argv[3]
		print("Running function: " + function_name +"("+ var1 +", "+ var2 +")")
	elif(len(argv) == 5):
		function_name = argv[1]
		var1 = argv[2]
		var2 = argv[3]
		var3 = argv[4]
		print("Running function: " + function_name +"("+ var1 +", "+ var2 +", "+ var3 +")")
	elif(len(argv) == 6):
		function_name = argv[1]
		var1 = argv[2]
		var2 = argv[3]
		var3 = argv[4]
		var4 = argv[5]
		print("Running function: " + function_name +"("+ var +", "+ var2 +", "+ var3 +", "+ var4 +")")
	else:
		print("No functions currently contain more than 4 variables.")
		exit(1)

	

if (__name__ == "__main__"):
	main()
