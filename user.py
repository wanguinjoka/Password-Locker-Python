class User:
    '''
    class that generates new instances of users

    '''
    def __init__(self, username,password):

        self.username = username
        self.password = password

class Credentials(User):

    '''
    class that generates new instances of Credentials

    '''
    def __init__(self, appName, loginname, passwordUsed):

        self.appName = appName
        self.loginname = loginname
        self.passwordUsed = passwordUsed
