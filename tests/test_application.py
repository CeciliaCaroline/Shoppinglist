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


if __name__ == '__main__':
    unittest.main()
