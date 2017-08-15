import re


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
        # self.list_items = {}

    def create_list(self, list1):
        """"
        method to check if the list id exists, if not,  create a new list
        :param list1
        """
        if list1.list_id in self.lists.keys():
            return False
        elif list1.title in self.new_lists:
            return False

        else:
            self.lists[list1.list_id] = list1
            self.new_lists[list1.list_id] = list1.title
            return True

    def total_lists(self):
        """"
        method to return the total number of lists created
        """
        return len(self.lists)

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
        method to get all lists that have been created
        """
        return self.lists

    def get_list(self, list_id):
        """
        method to get single list corresponding to list id
        """
        if list_id in self.lists.keys():
            return self.lists[list_id]
        return None

    def del_list(self, list_id):
        """"
        method to delete an existing list
        :param list_id
        """
        if list_id in self.lists.keys():
            del self.lists[list_id]
            del self.new_lists[list_id]
            return True
        return None

    def check_valid_list(self, title):
        """
        method to check that list title does not contain any special characters
        """
        if re.match("^[a-zA-Z0-9\s]*$", title):
            return True
