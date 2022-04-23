# Tests
import unittest
import user

class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = user("James","Muriuki","abcd")

    def test_init(self):
        self.assertEqual(self.new_user.fname == "James")
        self.assertEqual(self.new_user.lname == "Muriuki")
        self.assertEqual(self.new_user.password == "abcd") 


if __name__ == "__main__":
    unittest.main()