from typing import List
from menu import list_bagels, list_toppings
from order import calculate_total, print_receipt

def prompt_items(prompt: str, valid_items: List[str]) -> List[str]:
    raw: str = input(prompt).strip()
    items: List[str] = [x.strip() for x in raw.split(",") if x.strip() in valid_items]
    return items

def main() -> None:
    print("👋 Welcome to Howdy Bagel Ordering System!\n")
    list_bagels()
    bagels: List[str] = prompt_items(
        "Enter bagels (comma separated): ",
        ["plain","sesame","everything","poppyseed","onion"]
    )

    list_toppings()
    toppings: List[str] = prompt_items(
        "Enter toppings (comma separated): ",
        ["cream_cheese","lox","tomato","onion"]
    )

    total: float = calculate_total(bagels, toppings)
    print_receipt(bagels, toppings, total)

if __name__ == "__main__":
    main()
