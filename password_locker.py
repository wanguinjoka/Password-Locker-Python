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

def main():
    print ('Welcome to Passwrd Locker:-Where you can save your passwords.')
    print ('To navigate through the site use this short cuts : nu-New user , log-login')
    short_code = input('enter short_code')
    if short_code == 'nu':
        print('Welcome new user:')
        appName = input('Enter username -').strip()
        password = input('Enter password').strip()

        save_user(create_user(username,password))

        print('New account created for:{ username } { password }')
    elif short_code == 'li':
        print(' ')
        print('To login, enter your account details:')
        username = input('Enter your first name - ').strip()
        password = str(input('Enter your password - '))
        user_exists = verify_user(username,password)
        if user_exists = username:
            print(" ")
            print(f'Welcome {user_name}. Please choose an option to continue.')
            print(' ')
            while True:

                print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {user_name}')
						break
