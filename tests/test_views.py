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
        app.secret_key = "sdgsdgsjbdvskdxljvs"

        self.login = self.app.post('/login', data=dict(email='c@gmail.com', password='12345'),
                                   follow_redirects=True)

    # Ensure signup page request successful
    def test_signup_page_route(self):
        result = self.app.get('/signup', content_type='html/text')
        self.assertEqual(result.status_code, 200, msg='Unsuccessful request')

    # Ensure signup page loads
    def test_signup_page_loads(self):
        result = self.app.get('/signup', content_type='html/text')
        self.assertTrue(b'Sign me Up!' in result.data)

    # Ensure signup page behaves correctly given correct credentials
    def test_correct_signup(self):
        result = self.app.post('/signup', data=dict(username='Cecilia', email='c@gmail.com', password='12345'),
                               follow_redirects=True)
        self.assertIn(b'You have been registered', result.data, msg='Incorrect signup')

    # Ensure signup page behaves correctly given incorrect credentials
    def test_incorrect_signup(self):
        result = self.app.post('/signup', data=dict(username='Cecilia', email='', password='12345'),
                               follow_redirects=True)
        self.assertIn(b'Sign me Up!', result.data)

    # Ensure login page request successful
    def test_login_page_route(self):
        result = self.app.get('/login', content_type='html/text')
        self.assertEqual(result.status_code, 200, msg='Unsuccessful request')

    # Ensure login page loads
    def test_login_page_loads(self):
        result = self.app.get('/login', content_type='html/text')
        self.assertTrue(b'Log In' in result.data)

    # Ensure login page behaves correctly given correct credentials
    def test_correct_login(self):
        result = self.app.post('/login', data=dict(email='c@gmail.com', password='12345'),
                               follow_redirects=True)
        self.assertIn(b'Log In', result.data, msg='Incorrect login')

    # Ensure login page behaves correctly given incorrect credentials
    def test_incorrect_login(self):
        result = self.app.post('/login', data=dict(email='cecilia@gmail.com', password='12345'),
                               follow_redirects=True)
        self.assertIn(b'Log In', result.data, msg='correct login')

    # Ensure logout page behaves correctly given correct credentials
    def test_logout(self):
        self.app.post('/login', data=dict(email='cecilia@gmail.com', password='12345'),
                      follow_redirects=True)
        result = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'You have been logged out', result.data, msg='correct login')

        # Ensure home page request successful

    def test_home_page_route(self):
        result = self.app.get('/home', content_type='html/text')
        self.assertEqual(result.status_code, 200, msg='Unsuccessful request')

        # Ensure home page loads

    def test_home_page_loads(self):
        result = self.app.get('/home', content_type='html/text')
        self.assertTrue(b'Click on My Lists to start creating lists', result.data)


if __name__ == '__main__':
    unittest.main()
