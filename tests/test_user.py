import unittest
from app.models.user import User
from app.models.list import List


class TestUser(unittest.TestCase):
    """
       Class to test if user can create, view, edit and delete a bucket list
    """

    def setUp(self):
        self.user = User('CeciliaCaroline', 'cecilia@gmail.com', '123456')
        self.new_list = List('Food', 'I want to buy food supplies', 'ASGTJVCDSR')

    def test_list_class(self):
        self.assertIsInstance(self.new_list, List, msg='Object is not an instance of the list class')

    def test_create_list(self):
        self.assertTrue(self.user.create_list(self.new_list))

    def test_bucket_to_create_already_exists(self):
        list1 = List('Food', 'I want to buy food supplies', 'ASGTJVCDSR')
        self.user.lists = {"ASGTJVCDSR": list1}
        self.assertFalse(self.user.create_list(list1))

    def test_new_list_stored_in_dictionary(self):
        self.assertEqual(type(self.user.get_lists()), dict, msg='Output is not a dictionary')

    def test_a_list_is_returned_when_an_id_is_specified(self):
        list1 = List('Food', 'I want to buy food supplies', 'ASGTJVCDSR')
        self.user.lists = {"ASGTJVCDSR": list1}
        self.assertEqual(self.user.get_list("ASGTJVCDSR"), list1)

    def test_none_is_returned_for_list_doesnot_exist(self):
        self.assertIsNone(self.user.get_list('ADGFUJV'))

    def test_edit_list(self):
        self.user.create_list(self.new_list)
        self.assertTrue(self.user.edit_list('ASGTJVCDSR', 'Travel', 'I want to buy travel ticket'))

    def test_list_to_edit_doesnt_exists(self):
        list1 = List('Food', 'I want to buy food supplies', 'ASGTJVCDSR')
        self.user.create_list(list1)
        self.assertFalse(self.user.edit_list('Travel', 'I want to buy travel ticket', 'AWDBFTHICG'))

    def test_del_list(self):
        self.user.create_list(self.new_list)
        self.assertTrue(self.user.del_list('ASGTJVCDSR'))

    def test_list_to_delete_doesnt_exists(self):
        list1 = List('Food', 'I love food', 'ASGTJVCDSR')
        self.user.create_list(list1)
        self.assertFalse(self.user.del_list('AWDBFTHICG'))


if __name__ == '__main__':
    unittest.main()
