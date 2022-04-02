def create_inventory(items: list) -> dict:
    inventory = dict()
    return add_items(inventory, items)


def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory
