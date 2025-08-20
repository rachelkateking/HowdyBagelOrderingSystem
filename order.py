from typing import List
from menu import MENU, TOPPINGS

HAPPY_HOUR_DISCOUNT = 0.2

def calculate_bagel_cost(items: List[str]) -> float:
    return sum(MENU[item] for item in items if item in MENU)

def calculate_topping_cost(items: List[str]) -> float:
    return sum(TOPPINGS[item] for item in items if item in TOPPINGS)

def calculate_hh_discount(subtotal: float) -> float:
    return subtotal * (1-HAPPY_HOUR_DISCOUNT)

def calculate_total(bagels: List[str], toppings: List[str]) -> float:
    subtotal: float = calculate_bagel_cost(bagels) + calculate_topping_cost(toppings)
    subtotal = calculate_hh_discount(subtotal)
    return round(subtotal, 2)

def print_receipt(bagels: List[str], toppings: List[str], total: float) -> None:
    print("\n----- Your Order -----")
    for b in bagels:
        print(f"Bagel: {b} ${MENU[b]:.2f}")
    for t in toppings:
        print(f"Topping: {t} ${TOPPINGS[t]:.2f}")
