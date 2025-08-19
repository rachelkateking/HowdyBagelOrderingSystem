import unittest
from order import calculate_bagel_cost, calculate_topping_cost, calculate_total

class TestOrder(unittest.TestCase):
    def test_calculate_bagel_cost(self):
        self.assertEqual(calculate_bagel_cost(["plain", "sesame"]), 4.5)

    def test_calculate_topping_cost(self):
        self.assertEqual(calculate_topping_cost(["cream_cheese", "lox"]), 4.0)

    def test_calculate_total(self):
        bagels = ["plain", "sesame"]
        toppings = ["cream_cheese"]
        total = calculate_total(bagels, toppings)
        self.assertEqual(total, 5.5)

if __name__ == "__main__":
    unittest.main()
