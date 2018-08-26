import random
import pyperclip
import string

class User:
    '''
    class that generates new instances of users

    '''
    user_list = []

    def __init__(self, username,password):

        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_user method saves usersobjects into user_list
        '''
        User.user_list.append(self)

    @classmethod
    def display_users(cls):
        '''
        method returns user lists
        '''
        return cls.user_list

class Credentials():

    credential_list =[]

    '''
    class that generates new instances of Credentials

    '''
    @classmethod
    def check_user(cls,username,password):
        '''
        method that checks if the username and password match entries in the user_list
        '''
        current_user= ''
        for user in User.user_list:
            if(user.username==username and user.password == password):
                current_user = user.username
        return current_user

    def __init__(self,appName, loginname, passwordUsed):


        self.appName = appName
        self.loginname = loginname
        self.passwordUsed = passwordUsed

    def save_credentials(self):
        '''
        this method saves the credentials of a users
        '''
        Credentials.credential_list.append(self)

    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate an 8 character password for a new credential
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list

    @classmethod
    def find_by_appName(cls, appName):
        '''
        Method that takes in a appName and returns a credential that matches that appName.

        Args:
            appName: appName to search for
        Returns :
            Credentials of person that matches the appName.
        '''

        for credentials in cls.credential_list:
            if credentials.appName == appName:
                return credentials
    @classmethod
    def appName_exist(cls, appName):
        '''
        Method that checks if a appName exists from the credential_list.
        Args:
            appName: appName to search if it exists
        Returns :
            Boolean: True or false depending if the appName_exists
        '''
        for credentials in cls.credential_list:
            if credentials.appName == appName:
                    return True

        return False

    @classmethod
    def copy_credential(cls,appName):
        '''
        Class method that copies a credential's info after the credential's site name is entered
        '''
        find_credential = Credential.find_by_appName(appName)
        return pyperclip.copy(find_credential.password)
