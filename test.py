# Tests
import unittest

from user import User
from user import Credentials
# from user import user

#a Test class that defines test cases
class Testuser(unittest.TestCase):

#setUp() method allows the definition of instructions to be executed before each test .
    def setUp(self):
        self.new_user = User("JM","abcd")

    def test_init(self):
        self.assertEqual(self.new_user.username,"JM")
        self.assertEqual(self.new_user.password,"abcd") 

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

# we are confirming that anything inside the if block should run only if this is the file that is currently being run
if __name__ == "__main__":
    unittest.main()