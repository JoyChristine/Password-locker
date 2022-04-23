# class of user
import random
import string


class User:


    userslist=[]
    def __init__(self,username,password):
        self.username = username
        self.password = password

    # every item is printed is put in the dict
    def save_user(self):
        User.userslist.append(self)
    

    # delete
    def delete_user(self):
        User.userslist.remove(self)

    # display users
    @classmethod 
    def display_user(cls):
        return cls.userslist

    @classmethod
    def find_by_number(cls,number):
        for user in cls.userslist:
            if user.password == number:
               return user

    @classmethod
    def find_user(cls,number):
        for user in cls.userslist:
            if user.username == number:
                return user

class Credentials:

    accounts =[]

    def __init__(self,accountusername,accountname,accountpassword):
        self.accountusername = accountusername
        self.accountname = accountname
        self.accountpassword = accountpassword

    def save_account(self):
        Credentials.accounts.append(self)
    
    # delete
    def delete_account(self):
        Credentials.accounts.remove(self)

    # display account
    @classmethod
    def display_account(cls):
        for account in cls.accounts:
            return cls.accounts

    @classmethod
    def find_by_number(cls,number):
        for account in cls.accounts:
            if account.accountusername == number:
                return True