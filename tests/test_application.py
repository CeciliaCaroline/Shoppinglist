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
