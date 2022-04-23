# class of user
import random
import string


class User:


    userslist=[]
    def __init__(self,fname,lname,username,password):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password

    # every item is printed is put in the dict
    def save_user(self):
        User.userslist.append(self)

class Credentials:

    accounts =[]

    def __init__(self,accountusername,accountname,accountpassword):
        self.accountusername = accountusername
        self.accountname = accountname
        self.accountpassword = accountpassword

    def save_account(self):
        Credentials.accounts.append(self)