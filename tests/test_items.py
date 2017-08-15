import unittest
from app.models.list import List
from app.models.item import ListItems


class TestBucketItems(unittest.TestCase):
    """
    Class to test create, edit, view and delete bucket items.
    """

    def setUp(self):
        self.list = List('TRAVEL', 'I want to travel the world', 'ASGTJVCDSR')
        self.new_item = ListItems('Food', '5', '$12', 'AWDBFTHICG')

    def test_create_list_items(self):
        self.assertTrue(self.list.create_list_items(self.new_item))

    def test_list_item_to_create_already_exists(self):
        list_item = ListItems('Paris', '1', 'AWDBFTHICG', '$12')
        self.list.list_items = {"AWDBFTHICG": list_item}
        self.assertFalse(self.list.create_list_items(list_item))

    def test_list_item_stored_in_dictionary(self):
        self.assertEqual(type(self.list.get_items()), dict, msg='Output is not a dictionary')

    def test_a_list_id_is_key_for_dictionary(self):
        list1 = List('Food', 'I want to buy food supplies', 'ASGTJVCDSR')
        self.list.list_items = {"ASGTJVCDSR": list1}
        self.assertEqual(self.list.get_item("ASGTJVCDSR"), list1)

    def test_none_is_returned_for_list_item_does_not_exist(self):
        self.assertIsNone(self.list.get_item('ADGFUJV'))

    def test_edit_list_item(self):
        self.list.create_list_items(self.new_item)
        self.assertTrue(self.list.edit_list_item('Food', '5', '$12', 'AWDBFTHICG'))

    def test_list_item_to_edit_doesnt_exists(self):
        list_item = ListItems('Food', '10', '$20', 'ASGTJVCDSR')
        self.list.create_list_items(list_item)
        self.assertFalse(self.list.edit_list_item('Jeans', '5', '$12', 'AWDBFTHICG'))

    def test_del_item(self):
        self.assertFalse(self.list.del_item('ASGTJVCDSR'))

    def test_item_to_delete_doesnt_exists(self):
        list_item = ListItems('Food', '10', '$20', 'ASGTJVCDSR')
        self.list.create_list_items(list_item)
        self.assertFalse(self.list.del_item('AWDBFTHICG'))


if __name__ == '__main__':
    unittest.main()
