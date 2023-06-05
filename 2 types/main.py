# Generic-типы с параметрами типов
from typing import List, Dict, Optional, Set, Tuple

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.capitalize() + " " + last_name.capitalize()
    return full_name

def get_items(item_a: int, item_b: float, item_c: bool, item_d: bytes):
    return item_a, item_b, item_c, item_d

def get_list(items: List[str]):
    for item in items:
        print(item.capitalize())

def get_tuple_set(items_t: Tuple[int, int, str], item_s: Set[bytes]):
    return items_t, item_s

def get_dict(item_d: Dict[str, float]):
    for key, value in item_d.items():
        print(key)
        print(value)

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

print(get_full_name("Alexandr", "t"))
print(get_items(30, 25.3, 1, 8))
get_list(["qwer", "asdf", "zxcv"])
print(get_tuple_set((1, 2, "3"), {4, 5, 6, 7, 8}))
get_dict({"key": 1.5})
say_hi(2)
print(get_person_name(Person(232)))