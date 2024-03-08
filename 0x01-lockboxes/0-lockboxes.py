#!/usr/bin/python3
"""
Determines if a set of boxes together contains the keys to unlock all boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list): A list of lists representing locked boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if boxes:
        keys_collected = [0]
        keys_needed = [i[0] for i in enumerate(boxes)]

        # Collect keys from all unlockable boxes starting with 0
        collect_keys(boxes, keys_collected)

        # Return True or False basedon whether collected keys match keys needed
        return sorted(keys_collected) == keys_needed
    else:
        # If no boxes are provided, consider them all unlocked
        return True


def collect_keys(boxes, keys_collected, current_box=0):
    """
    Recursively collects unique keys from all boxes.

    Args:
        boxes (list): A list of lists representing locked boxes and their keys.
        keys_collected (list): A list of keys collected so far.
        current_box (int): The current box number.

    Returns:
        None
    """
    for new_key in boxes[current_box]:
        if new_key not in keys_collected and new_key < len(boxes):
            keys_collected.append(new_key)
            collect_keys(boxes, keys_collected, new_key)
