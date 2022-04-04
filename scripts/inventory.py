def create_inventory(items: list) -> dict:
    """
    Takes a list of items and returns a dictionary containing the amount
    of each item
    """
    inventory = dict()
    return add_items(inventory, items)


def add_items(inventory: dict, items: list) -> dict:
    """
    Takes an inventory containing kay-value pairs of items and their 
    quantities and a list items to be added to the inventory to be 
    added to the inventory
    Returns the updated invetory
    """
    for item in items:  # O(n)
        if item in inventory:  # O(1)
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def decrement_items(inventory: dict, items: list) -> dict:
    """
    Takes an inventory containing key-value pairs of their items and 
    their quantities, and a list ot items to be removed from the invetory, 
    each item mention removes a unit.
    Returns the updated inventory
    """
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory: dict, item: str) -> dict:
    """
    Takes an invetory containig key-value pairs of items and their quantities
    and the name of an item.
    Removes the item and all its quantites from the inventory and
    returns the updates inventory
    """
    inventory.pop(item, None)
    return inventory


def list_inventory(inventory: dict) -> list:
    """
    Takes an invetory containing kay-value pairs of items and their quantites
    Returns a list of tuples with the item name and its quantity containing 
    those items with quantities greater than zero only
    """
    return [item for item in list(inventory.items()) if item[1] > 0]
