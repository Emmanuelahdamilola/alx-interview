#!/usr/bin/python3
""" 
Calculate the minimum operations necessary to duplicate a given character
to appear n times.
"""


def minOperations(n):
    """ 
    Calculate the minimum operations necessary to duplicate a given character
    to appear n times.
    """
    operation_count = 0
    character = 'H'
    buffer = ''

    while len(character) < n:

        # If target size n is cleanly divisible by current size
        if n % len(character) == 0:
            # Copy character contents to buffer
            buffer = character
            operation_count += 1

        # Paste buffer to character
        character += buffer
        operation_count += 1

    return operation_count
