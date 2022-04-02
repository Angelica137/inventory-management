def create_inventory(items: list) -> dict:
    """
    Takes a list of items and returns a dictionary containing the amount
    of each item
    """
    inventory = dict()
    return add_items(inventory, items)


def add_items(inventory: dict, items: list) -> dict:
    """
    Takes an inventory containing value pairs of items and their quantities
    and a list items to be added to the inventory to be added to the inventory
    Returns the updated invetory
    """
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory
