import unittest
from app import app


class TestViews(unittest.TestCase):
    """"
    Class to test the functionality of the routes of the application
    """

    def setUp(self):
        # propagate the exceptions to the test client
        app.testing = True

        # creates a test client
        self.app = app.test_client()

    # Ensure signup page request successful
    def test_signup_page_route(self):
        result = self.app.get('/signup', content_type='html/text')
        self.assertEqual(result.status_code, 200, msg='Unsuccessful request')

    # Ensure login page request successful
    def test_login_page_route(self):
        result = self.app.get('/login', content_type='html/text')
        self.assertEqual(result.status_code, 200, msg='Unsuccessful request')




if __name__ == '__main__':
    unittest.main()
