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

class Credentials(User):

    '''
    class that generates new instances of Credentials

    '''
    def __init__(self, appName, loginname, passwordUsed):

        self.appName = appName
        self.loginname = loginname
        self.passwordUsed = passwordUsed
