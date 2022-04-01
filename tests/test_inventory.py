from scripts.inventory import *


def test_create_inventory():
    items = ["coal", "wood", "wood", "diamond", "diamond", "diamond"]
    assert create_inventory(items) == {"coal": 1, "wood": 2, "diamond": 3}
