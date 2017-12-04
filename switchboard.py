#!/usr/bin/python3

import backend
from sys import argv

def main():
	#Display how to run script.
	if(len(argv) <= 1):
		print("----------------------------------------------------------------------")
		print("-                         Overview:			     	    -")
		print("----------------------------------------------------------------------")
		print("             From the terminal run this script.             	     ")
		print(" Include the function you would like to run without paranthesis.	     ")
		print("            Followed by your variables in order.              	     ")
		print("									     ")
		print(" Functions: check_user_password, check_user_exists, 		     ")
		print("		check_password_policy, and check_sudo_user_password	     ")
		print("									     ")
		print(" Format 1: python switchboard.py <function> <var1>, <var2>, etc..     ")
		print(" Format 2: python switchboard.py <function>			     ")
		print("				--> then follow instructions		     ")
		print("----------------------------------------------------------------------")
		exit(1)
	#Run a function.
	elif(len(argv) >= 2):
		#Run check_user_password_set function.
		if(argv[1] == "check_user_password_set"):
			if(len(argv) == 3):
				var1 = argv[2]
				if(backend.check_user_password_set(var1) == True):
					print("Password set.")
				else:
					print("Password not set.")
			else:
				print("Please enter a userName to check.")
				userName = input()
				if(backend.check_user_password_set(userName) == True):
					print("Password set.")
				else:
					print("Password not set.")

		#Run check_user_exists function.
		elif(argv[1] == "check_user_exists"):			
			if(len(argv) == 3):
				var1 = argv[2]
				if(backend.check_user_exists(var1) == True):
					print("User exists.")
				else:
					print("User does not exist.")
			else:
				print("Please enter a userName to check.")
				userName = input()
				if(backend.check_user_exists(userName) == True):
					print("User exists.")
				else:
					print("User does not exist.")

		#Run check_password_policy function.
		elif(argv[1] == "check_password_policy"):
			if(len(argv) == 6):
				var1 = int(argv[2])
				var2 = int(argv[3])
				var3 = int(argv[4])
				var4 = int(argv[5])
				if(backend.check_password_policy(var1, var2, var3, var4) == True):
					print("Password policy parameters match.")
				else:
					print("Password policy parameters do not match.")
			else:
				print("Number of possible attempts to change password:")
				changeTries = input()
				print("Maximum days password is valid:")
				maxDays = input()
				print("Maximum password length:")
				maxLen = input()
				print("Minimum password length:")
				minLen = input()
				if(backend.check_password_policy(changeTries, maxDays, maxLen, minLen) == True):
					print("Password policy parameters match.")
				else:
					print("Password policy parameters do not match.")
		#Run check_sudo_user_password function.
		elif(argv[1] == "check_sudo_user_password"):
			if(backend.check_sudo_user_password() == True):
				print("Sudo users must use passwords for sudo commands.")
			else:
				print("Sudo users don't need to use passwords for sudo commands.")
		#Function doesn't exist.
		else:
			print("Function not found.")
			exit(1)
	#Error
	else:
		quit()

	

if (__name__ == "__main__"):
	main()
