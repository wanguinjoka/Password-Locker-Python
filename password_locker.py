import pyperclip
from user import User
from user import Credentials

def create_user(username,password):
    '''
    function that creates a new user to the app
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    function to save a user
    '''
    User.save_user(user)

def verify_user(username,password):
    '''
    function that verify user inorder to create credentials
    '''
    checkverify_user = Credentials.check_user(username,password)
    return checkverify_user
