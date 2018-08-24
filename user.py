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

class Credentials(User):

    credential_list =[]

    '''
    class that generates new instances of Credentials

    '''
    def __init__(self, username,password,appName, loginname, passwordUsed):
        super().__init__(username,password)

        self.appName = appName
        self.loginname = loginname
        self.passwordUsed = passwordUsed

    def save_credentials(self):
        '''
        this method saves the credentials of a users
        '''
        Credentials.credential_list.append(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a credential that matches that username.

        Args:
            username: Username to search for
        Returns :
            Credentials of person that matches the username.
        '''

        for credentials in cls.credential_list:
            if credentials.username == username:
                return credentials
    # @classmethod
    # def display_credentials(cls):
    #     '''
    #     method returns credential lists
    #     '''
    #     if user.username == username:
    #         return cls.credential_list
    #
    #     else:
    #         return "Wrong username try a"
