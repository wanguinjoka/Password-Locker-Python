import unittest
from user import User
from user import Credentials # import credential class


class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("wangui","jbow*2") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"wangui")
        self.assertEqual(self.new_user.password,"jbow*2")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_save_multiple_users(self):
            '''
            test_save_multiple_users to check if we can save multiple users
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Testuser","pob1*") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)


    def test_display_all_users(self):
        '''
        test that returns a list of users usersobjects

        '''
        self.assertEqual(User.display_users(),User.user_list)



class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("wangu","pword","github","wanguijbow","jbow2*") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.appName,"github")
        self.assertEqual(self.new_credentials.loginname,"wanguijbow")
        self.assertEqual(self.new_credentials.passwordUsed,"jbow2*")


    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the Credentials object is saved into
        the credential list
        '''
        self.new_credentials.save_credentials() # saving the new Credentials
        self.assertEqual(len(Credentials.credential_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credential_list = []

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credential_list
            '''
            self.new_credentials.save_credentials()
            test_save_credentials = Credentials("testusername","testpassword","testapp","bowj","xoxo2*") # new user
            test_save_credentials.save_credentials()
            self.assertEqual(len(Credentials.credential_list),2)

    def test_find_credential_by_username(self):
        '''
        test to check if we can find a credential by username and display information
        '''

        self.new_credentials.save_credentials()
        test_credential = Credentials("testusername","testpassword","testapp","testloginused","testpasswordused") # new contact
        test_credential.save_credentials()

        found_credential = Credentials.find_by_username("testusername")

        self.assertEqual(found_credential.appName,test_credential.appName)
        self.assertEqual(found_credential.loginname,test_credential.loginname)
        self.assertEqual(found_credential.passwordUsed,test_credential.passwordUsed)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_credentials.save_credentials()
        test_credential = Credentials("testusername","testpassword","testapp","testloginused","testpasswordused") # new contact
        test_credential.save_credentials()

        user_exists = Credentials.user_exist("testusername")

        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()
