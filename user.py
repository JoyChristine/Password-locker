class User:
    """ Class User creates user accounts and saves their information"""

    def __init__(self, username, password):
        """
        Method to define the properties of each object
        """
        self.username = username
        self.password = password
    userslist = []

    def save_user(self):
        """
       Function to save user instance
        """
        self.userslist.append(self)

