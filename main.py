import secrets
import string
from credentials import Credentials



def create_new_account(accountname, accountpassword):
	new_credential = Credentials(accountname, accountpassword)
	return new_credential


def save_new_account(credentials):
	credentials.save_account()

def check_existing_account(name):
    	return Credentials.find_account_by_name(name)

def delete_account(credentials):
    	return Credentials.delete_account(credentials)

def find_account(accountname):
	return Credentials.find_account_by_name(accountname)

def display_account():
    	return Credentials.display_account()


# def check_existing_account(name):
# 	return Credentials.find_account_by_name(name)


# def display_account():
# 	return Credentials.display_account()


def delete_account(credentials):
	return Credentials.delete_account(credentials)

def passwordlocker():

	print("Welcome to Password Locker")
	print("\n")
	while True:
		
		# Doyou have an existing account
		print("Would you like to Create new account Or login to exising account? \nCreate account --> C \nLogin --> L")
		choice = input()
		if choice == "C":
			print("Create new username")
			newusername = input()

			print("Enter your password")
			newpassword = input()

			print("Confirm your password")
			confirmpassword = input()

			while confirmpassword != newpassword:
				print("Oops! Passwords do not match!")

				print("Enter your password")
				newpassword = input()

				print("Confirm your password")
				confirmpassword = input()

				print("\n")
			else:
				print(f"Success! An account was created by {newusername}")
				print(f"Username: {newusername} \nPassword: {newpassword}")
				print("\n")
				print("-"*100)
				print("Would you like to Login?")
				print("Enter your Username")
				loginUsername = input()
				print("Enter your password")
				loginPassword = input()
			  
				# print(f"Hi, {loginUsername}! You are logged in!")

				while loginUsername != newusername or loginPassword != newpassword:
					print("Please input correct username and password")
					print("\n")
					print("Enter your Username")
					loginUsername =input()
					print("\nEnter your password")
					loginPassword = input()
					# print(f"Hi, {loginUsername}! You are logged in!")
				else:
					print(f"Hi, {loginUsername}! You are logged in!")
					print("\n")
					print("-"*100)
					# print("What do you want to do?")
					print("WELCOME TO MAIN MENU")
					print("Choose options 1,2,3,4 or 5")
					print

				while True:
					print("\n")
					print("1.Add new Account")
					print("2.View saved accounts")
					print("3.Search saved accounts")
					print("4.Delete saved accounts")
					
					choice2 = input()

					if choice2 == '1':
						while True:
							print("-"*100)
							print("Add account? y/n")
							choice3 = input()

							if choice3 == 'y':
								print("Enter account name")
								accountname = input()
									# print("Enter your Username")
									# loginUsername =input()
								print("Would you like to enter your password or generate one? E/G")
								password = input()
								if password == "E":
									accountpassword = input()
										# print("Enter your password")
								
									print("Success! You have created a new account. See details below.")
									print(f"Account name: {accountname} \nPassword: {accountpassword}")  
									save_new_account(create_new_account(accountname, accountpassword))                          
								elif password == "G":
									letters = string.ascii_lowercase + string.digits + string.punctuation
									accountpassword = ''.join(secrets.choice(letters) for i in range(1,10))
									print("Success! You have created a new account. See details below.")
									print(f"Account name: {accountname} \nPassword: {accountpassword}")  
									print("\n")
									save_new_account(create_new_account(accountname, accountpassword))
								else:
									print("Invalid! Please enter Valid choice")
									print("\n")
									print("-"*100)
									# print("Please choose E or G")

								# save_new_account(create_new_account(accountname, accountpassword))
										# save_account(create_account(accountname,accountpassword))
							elif choice3 == 'n':
								break
							else:
								print("Use either y or n")



					elif choice2 == '2':
						while True:
    
							print(" Here's a list of accounts saved")
							if display_account():
								for account in display_account():
									print(f"Account Name:{account.accountname}")
									print(f"Password:{account.accountpassword}")
									print("\n")
									print("-"*100)
							else:
								print("Oops!Seems you have no accounts yet!")
							print("Back to Main menu y/n")
							option = input().lower()
							if option == "y":
								break

							elif option == "n":
								continue
							else:
								print("Enter a valid option")
								
					  
					elif choice2 == '3':
						print("\n")
						print("-"*100)
						print("Search account by name")
						option1 = input()
						if check_existing_account(option1):
							searchaccount = find_account(option1)
							print("Account Found!")
							print(f"Account name: {searchaccount.accountname}")
						else: print("That Account does not exist")
					# delete
					elif choice2 == '4':
    					
						print("THIS OPTION WILL DELETE ALL YOUR ACCOUNT")
						print("Search account by name")
						option2 = input()
						if check_existing_account(option2):
							searchaccount = find_account(option2)
							print("Account Found!")
							print(f"Account name: {searchaccount.accountname}")
							print(f"Are you sure you want to delete {searchaccount.accountname} y/n")
							option3 = input()
							if option3 == 'y':
								delete_account(searchaccount)
								print("Account Deleted!")
								print("\n")
								print("-"*100)
							elif option3 == 'n':
								continue
							else:
								print("Choose y/n")
						else: 
							print("That Account does not exist")
							print("-"*100)

					
					else:
						print("Invalid choice! Choose from the options below!")
						continue
# *****************************************************************************************************************************************
		# IF USER WANTS TO LOGIN
		elif choice == "L":
			print("Enter your username")
			existingusername = input()

			print("Enter your password")
			existingpassword = input()

			if existingusername != "person" or existingpassword != "11111":
				print("Incorrect! Account username is person & password is 11111")
				print("\n")
				print("Enter your username")
				existingusername = input()
				print("Enter your password")
				existingpassword = input()

			elif existingusername == "person" and existingpassword == "11111":
				print("\n")
				print("You have successfully logged in ")
				print("-"*100)
				print("Select an option below")

			while True:
					print("\n")
					print("1.Add new Account")
					print("2.View saved accounts")
					print("3.Search saved accounts")
					print("4.Delete saved accounts")
					
					choice2 = input()

					if choice2 == '1':
						while True:
							print("-"*100)
							print("Add account? y/n")
							choice3 = input()

							if choice3 == 'y':
								print("Enter account name")
								accountname = input()
									# print("Enter your Username")
									# loginUsername =input()
								print("Would you like to enter your password or generate one? E/G")
								password = input()
								if password == "E":
									accountpassword = input()
										# print("Enter your password")
								
									print("Success! You have created a new account. See details below.")
									print(f"Account name: {accountname} \nPassword: {accountpassword}")  
									save_new_account(create_new_account(accountname, accountpassword))                          
								elif password == "G":
									letters = string.ascii_lowercase + string.digits + string.punctuation
									accountpassword = ''.join(secrets.choice(letters) for i in range(1,10))
									print("Success! You have created a new account. See details below.")
									print(f"Account name: {accountname} \nPassword: {accountpassword}")  
									print("\n")
									save_new_account(create_new_account(accountname, accountpassword))
								else:
									print("Invalid! Please enter Valid choice")
									print("\n")
									print("-"*100)
									# print("Please choose E or G")

								# save_new_account(create_new_account(accountname, accountpassword))
										# save_account(create_account(accountname,accountpassword))
							elif choice3 == 'n':
								break
							else:
								print("Use either y or n")



					elif choice2 == '2':
						while True:
    
							print(" Here's a list of accounts saved")
							if display_account():
								for account in display_account():
									print(f"Account Name:{account.accountname}")
									print(f"Password:{account.accountpassword}")
									print("\n")
									print("-"*100)
							else:
								print("Oops!Seems you have no accounts yet!")
							print("Back to Main menu y/n")
							option = input().lower()
							if option == "y":
								break

							elif option == "n":
								continue
							else:
								print("Enter a valid option")
								
					  
					elif choice2 == '3':
						print("\n")
						print("-"*100)
						print("Search account by name")
						option1 = input()
						if check_existing_account(option1):
							searchaccount = find_account(option1)
							print("Account Found!")
							print(f"Account name: {searchaccount.accountname}")
						else: print("That Account does not exist")
					# delete
					elif choice2 == '4':
    					
						print("THIS OPTION WILL DELETE ALL YOUR ACCOUNT")
						print("Search account by name")
						option2 = input()
						if check_existing_account(option2):
							searchaccount = find_account(option2)
							print("Account Found!")
							print(f"Account name: {searchaccount.accountname}")
							print(f"Are you sure you want to delete {searchaccount.accountname} y/n")
							option3 = input()
							if option3 == 'y':
								delete_account(searchaccount)
								print("Account Deleted!")
								print("\n")
								print("-"*100)
							elif option3 == 'n':
								continue
							else:
								print("Choose y/n")
						else: 
							print("That Account does not exist")
							print("-"*100)

					
					else:
						print("Invalid choice! Choose from the options below!")
						continue
   
if __name__ == "__main__":
	passwordlocker()





