import re


class List:
    def __init__(self, title, description, list_id):
        self.title = title
        self.description = description
        self.list_id = list_id
        self.list_items = {}
        self.new_list_items = {}
        self.done = []
        self.undone = []

    def create_list_items(self, new_item):
        """"
        method to check if item id already exists, if not, create a new list item
        :param new_item
        """
        if new_item.item_id in self.list_items.keys():
            return False
        elif new_item.item in self.new_list_items:
            return False

        else:
            self.list_items[new_item.item_id] = new_item
            self.new_list_items[new_item.item_id] = new_item.item
            return True

    def edit_list_item(self, title, quantity, item_id, price, status):
        """"
        method to edit an existing item
        :param item_id
        :param title
        :param quantity
        :param price
        :param status
        """
        if item_id in self.list_items.keys():
            edit_list_item = self.list_items[item_id]
            edit_list_item.title = title
            edit_list_item.quantity = quantity
            edit_list_item.price = price
            edit_list_item.status = status
            return True
        return False

    def get_items(self):
        return self.list_items

    def get_item(self, item_id):
        if item_id in self.list_items.keys():
            return self.list_items[item_id]

    def del_item(self, item_id):
        """"
        method to delete an existing item
        :param item_id
        """
        if item_id in self.list_items.keys():
            del self.list_items[item_id]
            del self.new_list_items[item_id]
            return True
        return False

    def check_valid_items(self, item):
        if re.match("^[a-zA-Z0-9\s]*$", item):
            return True

    def get_done_status(self, new_item):
        new_item.status == 'Done'
        self.done.append(new_item)

        # return True

    def get_undone_status(self, new_item):
        new_item.status == 'Not Done'
        self.undone.append(new_item)
