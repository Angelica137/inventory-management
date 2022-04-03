from scripts.inventory import *


def test_create_inventory():
    items = ["coal", "wood", "wood", "diamond", "diamond", "diamond"]
    assert create_inventory(items) == {"coal": 1, "wood": 2, "diamond": 3}


def test_add_items():
    inventory = {"coal": 1}
    items = ["wood", "iron", "coal", "wood"]
    assert add_items(inventory, items) == {"coal": 2, "wood": 2, "iron": 1}


def test_decrement_items():
    inventory = {"coal": 3, "diamond": 1, "iron": 5}
    items = ["diamond", "coal", "iron", "iron"]
    assert decrement_items(inventory, items) == {
        "coal": 2, "diamond": 0, "iron": 3}


def test_decrement_items_0_count():
    inventory = {"coal": 3, "diamond": 0, "iron": 5}
    items = ["diamond", "coal", "iron", "iron"]
    assert decrement_items(inventory, items) == {
        "coal": 2, "diamond": 0, "iron": 3}


def test_remove_item():
    inventory = {"coal": 2, "wood": 1, "diamond": 2}
    assert remove_item(inventory, "coal") == {"wood": 1, "diamond": 2}
