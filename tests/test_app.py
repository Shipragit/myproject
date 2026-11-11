import unittest

from app import get_message


class AppTest(unittest.TestCase):
    def test_default_message(self):
        self.assertEqual(get_message(), "Hello, World!")

    def test_custom_message(self):
        self.assertEqual(get_message("Alice"), "Hello, Alice!")


if __name__ == "__main__":
    unittest.main()
