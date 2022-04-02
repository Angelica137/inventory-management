from scripts.inventory import *


def test_create_inventory():
    items = ["coal", "wood", "wood", "diamond", "diamond", "diamond"]
    assert create_inventory(items) == {"coal": 1, "wood": 2, "diamond": 3}


def test_add_items():
    inventory = {"coal": 1}
    items = ["wood", "iron", "coal", "wood"]
    assert add_items(inventory, items) == {"coal": 2, "wood": 2, "iron": 1}
