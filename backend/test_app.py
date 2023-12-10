import unittest
from app.app import app, db

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_register(self):
        response = self.app.post('/register', json={
            'username': 'test',
            'password': 'test'
        })
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = self.app.post('/login', json={
            'username': 'test',
            'password': 'test'
        })
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()