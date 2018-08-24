import unittest
from user import User
from user import Credentials # import credential class


class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("wangui","jbow*2") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"wangui")
        self.assertEqual(self.new_user.password,"jbow*2")



if __name__ == '__main__':
    unittest.main()
