import unittest
from app.models.application import Application
from app.models.user import User


class TestApplication(unittest.TestCase):
    """
    Class to test the user authentication, both the registration
    and login.
    """

    def setUp(self):
        self.user = User('CeciliaCaroline', 'cecilia@gmail.com', '123456')
        self.app = Application()

    def test_user_is_registered(self):
        self.assertTrue(self.app.register(User('CeciliaCaroline', 'cecilia@gmail.com', '123456')))

    def test_user_login(self):
        self.app.register(self.user)
        self.assertTrue(self.app.login('cecilia@gmail.com', '123456'))

    def test_invalid_email_type_at_signup(self):
        self.user = self.app.register(self.user)
        self.user1 = User('CeciliaCaroline', 'cecilia', '123456')
        new_user = self.app.register(self.user1)
        self.assertEqual(new_user, self.user, msg='Input is not an email')

    def test_for_empty_password_at_signup(self):
        self.user = self.app.register(self.user)
        self.user1 = User('CeciliaCaroline', 'cecilia', ' ')
        new_user = self.app.register(self.user1)
        self.assertEqual(new_user, self.user, msg='Password is empty')

    def test_invalid_email_type_at_login(self):
        self.user = self.app.login('cecilia@gmail.com', '123456')
        new_user = self.app.login('cecilia.com', '123456')
        self.assertEqual(new_user, self.user, msg='Input is not an email')

    def test_for_empty_password_at_login(self):
        self.user = self.app.login('cecilia@gmail.com', '123456')
        new_user = self.app.login('cecilia@gmail.com', ' ')
        self.assertEqual(new_user, self.user, msg='Password is empty')

    def test_for_invalid_password_at_login(self):
        self.user1 = self.app.login('cecilia@gmail.com', '123456')
        new_user = self.app.login('cecilia@gmail.com', 'pass ')
        self.assertEqual(new_user, self.user1, msg='The password is invalid')


if __name__ == '__main__':
    unittest.main()
