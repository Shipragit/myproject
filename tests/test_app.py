import unittest

from app import app, get_message


class AppTest(unittest.TestCase):
    def test_default_message(self):
        self.assertEqual(get_message(), "Hello, World!")

    def test_custom_message(self):
        self.assertEqual(get_message("Alice"), "Hello, Alice!")

    def test_root_endpoint(self):
        client = app.test_client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello, World!", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
