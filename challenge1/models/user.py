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

    def create_list(self, list):
        """"
        method to check if the list id exists, if not,  create a new list
        :param list
        """
        if list.list_id in self.lists.keys():
            return False
        elif list.title in self.new_lists:
            return False

        else:
            self.lists[list.list_id] = list
            self.new_lists[list.list_id] = list.title
            return True

    def edit_list(self, list_id, title, description):
        """"
        method to edit the title of an existing bucket list
        :param list_id
        :param title
        :param description
        """
        if list_id in self.lists.keys():
            edited_list = self.lists[list_id]
            edited_list.title = title
            edited_list.description = description
            return True
        return False

    def get_lists(self):
        """
        method to get all lists
        """
        return self.lists

    def get_list(self, list_id):
        """
        method to get single list corresponding to list id
        """
        if list_id in self.lists.keys():
            return self.lists[list_id]
        return None
