import unittest
from user import User
from user import Credentials # import credential class
import pyperclip

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

    def test_check_user(self):
        '''
		Function to test whether the login in function check_user works as expected
		'''
        self.new_user = User('njoka2','pswdloc')
        self.new_user.save_user()
        user2 = User('johndoe','passW2')
        user2.save_user()

        for user in User.user_list:
            if user.username == user2.username and user.password == user2.password:
                current_user = user.username
        return current_user

        self.assertEqual(current_user,Credential.check_user(user2.password,user2.username))

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("github","wanguijbow","jbow2*") # create user object


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
        '''g
        test_save_multiple_credentials to check if we can save multiple credentials
        objects to our credential_list
        '''
        self.new_credentials.save_credentials()
        test_save_credentials = Credentials("testapp","bowj","xoxo2*") # new user
        test_save_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_display_credentials(self):
        '''
        Test to check if the display_credentials method, displays the correct credentials.
        '''
        self.new_credentials.save_credentials()
        facebook = Credentials('facebook','bowjoe','testpass')
        facebook.save_credentials()
        gmail = Credentials('Gmail','maryjoe','passw2')
        gmail.save_credentials()
        self.assertEqual(len(Credentials.display_credentials(facebook.loginname)),2)

    def test_find_by_appName(self):
        '''
        test to check if we can find a credential by appname and display information
        '''

        self.new_credentials.save_credentials()
        facebook = Credentials('facebook','bowjoe','testpass')
        facebook.save_credentials()
        credentials_exists = Credentials.find_by_appName('facebook')
        self.assertEqual(credentials_exists,facebook)


    def test_copy_credential(self):
        '''
        test to confirm we are copying the credentials
        '''
        self.new_credentials.save_credentials()
        facebook = Credentials('facebook','bowjoe','testpass')
        facebook.save_credentials()
        find_credential = None

        for credentials in Credentials.credential_list:
            find_credential =Credentials.find_by_appName(credentials.appName)
            return pyperclip.copy(find_credential.passwordUsed)
        Credentials.copy_credential(self.new_credentials.appName)
        self.assertEqual('testpass',pyperclip.paste())
        print(pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
