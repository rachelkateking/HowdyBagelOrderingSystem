from typing import Dict

MENU: Dict[str, float] = {
    "plain": 2.00,
    "sesame": 2.50,
    "everything": 3.00,
    "poppyseed": 2.50,
    "onion": 2.75,
}

TOPPINGS: Dict[str, float] = {
    "cream_cheese": 1.00,
    "lox": 3.00,
    "tomato": 0.50,
    "onion": 0.25,
}

def list_bagels() -> None:
    print("Available bagels:")
    for name, price in MENU.items():
        print(f" - {name:12} ${price:.2f}")

def list_toppings() -> None:
    print("Available toppings:")
    for name, price in TOPPINGS.items():
        print(f" - {name:12} ${price:.2f}")
