class User:
    def __init__(self, username, email, password):
        """"
        method to initialize user attributes
        :param username
        :param email
        :param password
        """
        self.username = username
        self.email = email
        self.password = password
        self.lists = {}
        self.new_lists = {}
        self.list_items = {}
        