#!/usr/bin/python3

def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed to result in n H chars.

    :param n: Target number of H characters
    :type n: int
    :return: The min number of operations needed to reach n H character, or 0
    :rtype: int
    """

    if n <= 1:
        return 0

    operations = 0
    current = 1
    clipboard = 0

    while current < n:
        if n % current == 0:
            # Use Copy All followed by Paste (n // current - 1) times
            operations += n // current
            clipboard = current
            current *= n // current
        else:
            # Use Paste to increase the current count
            operations += 1
            current += clipboard

    return operations
