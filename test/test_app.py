import datetime
import unittest

from app import app  # Импортируем приложение из app.py

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_even_func(self):
        response = self.app.get('/even/12')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'12 is <b>even</b>', response.data)

    def test_odd_func(self):
        response = self.app.get('/even/13')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'13 is odd', response.data)
    def test_odd_func_negative(self):
        response = self.app.get('/even/14')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'13 is odd', response.data)

    def test_times_func(self):
        response = self.app.get('/time')
        response_data = response.data.decode('utf-8')
        self.assertEqual(response_data, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    unittest.main()