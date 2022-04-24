import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    """Test class that defines test cases for the credentials class"""

    def setUp(self):
        """ Set up method to run before each test cases."""
        self.new_credentials = Credentials("Twitter", "mypassword")

    def tearDown(self):
        """ Clean up method to run after each test cases."""
        Credentials.credentials_list = []


    def test_init(self):
        """ test_init test case to test if the object is initialized properly"""

        self.assertEqual(self.new_credentials.accountname, "Twitter")
        self.assertEqual(self.new_credentials.accountpassword, "mypassword")

    def test_save_credentials(self):
        """ test_save_credentials tests if the account object is saved in the credential list"""
        
        self.new_credentials.save_account()
        self.assertEqual(len(Credentials.credentials_list), 1)


    def test_display_all_credentials(self):
        """ test_display_all_credentials tests if all accounts saved can be displayed"""
        
        self.assertEqual(Credentials.display_account(), Credentials.credentials_list)

    

    def test_save_multiple_credentials(self):
        """Method that saves multiple credentials"""

        self.new_credentials.save_account()
        new_test_credential = Credentials("Twitter", "mypassword")
        new_test_credential.save_account()
        self.assertEqual(len(Credentials.credentials_list), 2)



    def test_find_credential_by_name(self):
        """Method that finds an account by name"""
        self.new_credentials.save_account()
        new_test_credential = Credentials("Twitter", "mypassword")
        new_test_credential.save_account()

        found_credential = Credentials.find_account_by_name("Twitter")

        self.assertEqual(found_credential.accountname, new_test_credential.accountname)



if __name__ == '__main__':
    unittest.main()
