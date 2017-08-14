import random
import string


class Application:
    def __init__(self):
        self.users = {}

    def register(self, user):
        """"
        method to register new users
        :param user
        """
        if user.email in self.users.keys():
            return False
        else:
            self.users[user.email] = user
            return True

    def login(self, email, password):
        """"
        method to login users who have already registered

        :param email
        :param password
        """
        if email in self.users.keys():
            user = self.users[email]
            if user.password == password:
                return True
            return False

    def get_user(self, email):
        """"
        method to return a user  corresponding to an specific email
        :param email
        """
        if email in self.users.keys():
            return self.users[email]
        return None

    def random_id(self):
        """"
        method to generate random id
        """
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
