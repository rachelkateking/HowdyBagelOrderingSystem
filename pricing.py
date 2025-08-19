# pricing.py
# Price calculation and discount rules
from datetime import datetime, time
from typing import Optional

from menu import get_price
from toppings import toppings_cost

# Change these in branches to demonstrate conflicts during the demo:
TAX_RATE = 0.095  # 9.5% (Tacoma illustrative value)

def line_item_subtotal(bagel_name: str, qty: int, topping_names):
    if qty <= 0:
        raise ValueError("Quantity must be positive")
    base = get_price(bagel_name)
    extras = toppings_cost(topping_names)
    return round(qty * (base + extras), 2)

def apply_discounts(subtotal: float, code: Optional[str] = None, now=None) -> float:
    total = subtotal
    # Simple code-based promo
    if code:
        code = code.strip().upper()
        if code == "STUDENT10":
            total *= 0.90
        elif code == "WELCOME5":
            total -= 5.00
    return max(round(total, 2), 0.0)

def total_with_tax(subtotal: float) -> float:
    return round(subtotal * (1 + TAX_RATE), 2)

def compute_total(bagel_name: str, qty: int, topping_names, code: Optional[str] = None, now=None) -> dict:
    """Compute a detailed pricing breakdown for a single-line order."""
    sub = line_item_subtotal(bagel_name, qty, topping_names)
    discounted = apply_discounts(sub, code=code, now=now)
    taxed = total_with_tax(discounted)
    return {
        "subtotal": sub,
        "discounted_subtotal": discounted,
        "taxed_total": taxed,
    }
