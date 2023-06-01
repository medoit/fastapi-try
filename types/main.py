# Generic-типы с параметрами типов
from typing import List, Dict, Set, Tuple

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.capitalize() + " " + last_name.capitalize()
    return full_name

def get_items(item_a: int, item_b: float, item_c: bool, item_d: bytes):
    return item_a, item_b, item_c, item_d

def get_list(items: List[str]):
    for item in items:
        print(item.capitalize())

print(get_full_name("Alexandr", "t"))
print(get_items(30, 25.3, 1, 8))

get_list(["qwer", "asdf", "zxcv"])