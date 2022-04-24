import unittest
from user import User


class TestUser(unittest.TestCase):
    """Test class that defines test cases for the user class"""

    def setUp(self):
        """SetUp method is run before each test case"""
        self.new_user = User("Twitter", "mypassword")

    def test_init(self):
        """ test_init test case to test if the object is initialized properly"""
        self.assertEqual(self.new_user.username, "Twitter")
        self.assertEqual(self.new_user.password, "mypassword")

    def test_save_user(self):
        """Test_save_user test case to test if the object is saved properly"""
        self.new_user.save_user()
        self.assertEqual(len(User.userslist), 1)


if __name__ == '__main__':
    unittest.main()
