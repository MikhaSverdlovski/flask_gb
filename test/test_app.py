import unittest

from app import app  # Импортируем приложение из app.py

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()  # Используем тестовый клиент Flask
        self.app.testing = True

    def test_even_func(self):
        response = self.app.get('/even/12')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'12 is <b>even</b>', response.data)  # Проверяем корректность ответа


if __name__ == '__main__':
    unittest.main()