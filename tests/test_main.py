import unittest
from unittest.mock import patch
from main import prompt_items

class TestMain(unittest.TestCase):
    @patch("builtins.input", return_value="plain, sesame, everything")
    def test_prompt_items(self, mock_input):
        valid_items = ["plain", "sesame", "everything", "onion"]
        items = prompt_items("Enter items: ", valid_items)
        self.assertEqual(items, ["plain", "sesame", "everything"])

if __name__ == "__main__":
    unittest.main()
