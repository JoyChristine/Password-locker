# import pyperclip
import string
import secrets

from user import Credentials
from user import User

def create_user(fname,lname,username,password):
    new_user = User(fname,lname,username,password)
    return new_user
# save  user
def save_user(user):
    user.save_user()
    print("Success! An account was created. See details below")
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

# save account user
def save_account(user):
    user.save_account()

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
    while True:
        print("Welcome to Password Locker, My name is Bot")
        # Doyou have an existing account
        print("Would you like to Login or Sign up to existing account? L/S")
        choice = input()
        if choice == "S":
            print("Create new account")
            print("-"*100)
            print("Enter your first name")
            fname = input()
            print("Enter your last name")
            lname = input()
            print("Enter your username")
            username = input()
            print("Enter your password")
            password = input()
            save_user(create_user(fname,lname, username, password))
            # print("Success! An account was created. See details below")
            print("-"*100)
            print(f"Name: {fname} {lname} \nUsername: {username} \nPassword: {password}")
            
            print("Use the details to login to account \n")
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
                    accountusername=loginUsername
                    print("Account name")
                    accountname=input()
                    print("Enter own password or generate  E/G")
                    choice3 = input()
                    if choice3 == "E":
                            letters = string.ascii_lowercase + string.digits + string.punctuation
                            accountpassword = ''.join(secrets.choice(letters)
                             for i in range(5,10))
                            print(f"Password: {accountpassword}")
                    elif choice3 == "G":
                        print("Enter password")
                        accountpassword =input()
                    else:
                        print("Invalid choice")
                    save_account(create_account(accountusername,accountname,accountpassword))
                    print("\n")
                    print(f"username: {accountusername} \n Account name: {accountname} \n Password: {accountpassword}")   

                elif choice2 == "V":
                    if find_account(accountusername):
                        print("Here's a list of your Accounts")

                        for user in display_account():
                            print(f"Account: {user.accountname} \n Password: {user.accountpassword} \n")
                    else:
                        print("Invalid")
                else:
                    print("Please input C or V")
                
            else:
                print("Invalid")
        else:
            print("Invalid")

       
   
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

    