# import pyperclip
import string
import secrets

from user import Credentials
from user import User

def create_user(username,password):
    new_user = User(username,password)
    return new_user
# save  user
def save_user(user):
    user.save_user()
    # print(f"Success! An account was created by {username}. See details below")
# find user
def find_user(number):
    return User.find_by_number(number)
#display user
def display_users():
   return User.display_users()
 
# delete user
def delete_user(user):
    user.delete_user()

# create account
def create_account(accountusername,accountname,accountpassword):
    newaccount = Credentials(accountusername,accountname,accountpassword)
    return newaccount

def generate_Password():

    auto_password=Credentials.generateNewPassword()
    return auto_password
# save account user
def save_account(user):
    user.save_account()
    print("Success! An account was created. See details below")

# find account user
def find_account(number):
    return Credentials.find_by_number(number)

# display account
def display_account(number):
    return Credentials.display_by_number(number)

# delete account
def delete_account(user):
    user.delete_account()
    
def passwordlocker():
    accountusername = ""
    user = ""
    accountpassword = ""
    while True:
        print("Welcome to Password Locker")
        # Doyou have an existing account
        print("Would you like to Create new account Or login to exising account? \nCreate account --> C \nLogin --> L")
        choice = input()
        if choice == "C":
            print("Create new account")
            print("-"*100)
            
            print("Enter your username")
            username = input()
            print("Enter your password")
            password = input()
            print("\n \n")
            save_user(create_user(username, password))
            print(f"Success! An account was created by {username}. See details below")
            # print("-"*100)
            print(f"Username: {username} \nPassword: {password}")
            # print(f"Hi {username}, thanks for using Password locker")
            print("-"*100)
        elif choice == "L":
            print("Enter your username")
            loginUsername=input()
            print("Enter your password")
            loginPassword=input()
            if find_user(loginPassword):
                print("\n")
                print("Create new account or view existing ones? C/V")
                choice2 = input()
                if choice2 == "C":
                    print("Create new account")
                    # accountusername=loginUsername
                    # print("Account Username")
                    accountusername=loginUsername
                    # accountusername = input()
                    print("Account name")
                    accountname=input()
                    
                    print("Enter own password or generate  E/G")
                    choice3 = input()
                    if choice3 == "G":
                        accountpassword = generate_Password()
                    elif choice3 == "E":
                        accountpassword=input()
                        print("Enter password")
                        
                       
                    else:
                        print("Invalid choice")
                        print("Enter own password or generate  E/G")
                    save_account(create_account(accountname,accountusername,accountpassword))
                    print("\n")
                    print(f"New account details \nusername: {accountusername} \nAccount name: {accountname} \nPassword: {accountpassword}")   
                    print("\n")
                elif choice2 == "V":
                    if find_account(accountusername):
                        print("List of accounts you have")

                        for user in display_account():
                            print(f"Account: {user.accountname} \n Password: {user.accountpassword} \n") 
                            print("\n")
                            # NOT WORKING
                    else:
                        print("Invalid choice 1")
                        print("\n")
                else:
                    print("Please input C or V")
                    print("\n")
                
            else:
                print("Invalid choice 2")
                print("\n")

        else:
            print("Invalid choice! Choose C or L")
            print("\n \n")
       
   
if __name__ == "__main__":
    passwordlocker()














# # Created a dictionary of accounts + passwords
# mypasswords = {'twitter':'mytwitterpassword',
#                 'behance':'mybehancepassword'
#                 ,'facebook':'myfacebookpassword'
#                 ,'slack':'myslackpassword'
#             }
# repeat_forever = True

# def get_mypassword():
#     for i in mypasswords:
#         print(i)
#         # Print out account + password
#         # print(i + "-"+mypasswords[i]) 
#         # 
# # Get password and copy paste it
#     try:
#         i_selected = input("Which account password do you want? ").lower()
#         selected_password = mypasswords[i_selected]
#         pyperclip.copy(selected_password)
#         print("----------------------------------------------------------")
#         print("Password for your" + i_selected + " account has been copied to clipboard")
#         print("----------------------------------------------------------")
#     except:
#         print("Please enter valid account name.")
#         get_mypassword()


# get_mypassword()


# while repeat_forever:
#     # repeat_forever = True
#     get_another_password = input("Get new password? y/n")

#     if get_another_password == "y":
#             get_mypassword()
#     else:
#             repeat_forever = False
#             print("Okay")

    