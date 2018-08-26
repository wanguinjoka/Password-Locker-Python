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

def generate_password():
    '''
    function that generate a random password
    '''
    gen_pass = Credentials.generate_password()
    return gen_pass

def create_credentials(appName,loginname,passwordUsed):
    '''
    function that creates new credentials

    '''
    new_credentials=Credentials(appName,loginname,passwordUsed)
    return new_credentials

def save_credentials(credentials):
    '''
    function to save credentials
    '''
    Credentials.save_credentials(credentials)

def display_credentials(username):
    '''
    function that displays credentials saved by user
    '''
    return Credentials.display_credentials(username)

def copy_credential(appName):
    '''
    function to copy credentials to clipboard
    '''

    return Credentials.copy_credential(appName)
