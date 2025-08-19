import unittest
from menu import MENU, TOPPINGS, list_bagels, list_toppings

class TestMenu(unittest.TestCase):
    def test_menu_contains_items(self):
        self.assertIn("plain", MENU)
        self.assertIn("lox", TOPPINGS)

    def test_list_functions_run(self):
        # just ensure they execute without error
        list_bagels()
        list_toppings()

if __name__ == "__main__":
    unittest.main()
