# import pyperclip

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

    