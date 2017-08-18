class ListItems:
    """"
    List items class
    """
    def __init__(self, title, quantity, price, status, item_id):
        """"
        method to initialize list item attributes
        """
        self.title = title
        self.quantity = quantity
        self.item_id = item_id
        self.price = price
        self.status = status

