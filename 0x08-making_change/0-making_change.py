#!/usr/bin/python3
"""
This script calculates the fewest number of coins required to meet a given amount.
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given amount.

    Args:
        coins (list): List of coin values in possession.
        total (int): The given amount.

    Returns:
        int: Fewest number of coins needed to meet total.
             - If total is 0 or less, return 0.
             - If total cannot be met by any combination of coins, return -1.
    """
    if not isinstance(total, int) or not isinstance(coins, list):
        return -1

    if total <= 0:
        return 0

    try:
        min_coins = [float('inf') for _ in range(total + 1)]
        min_coins[0] = 0

        for i in range(1, total + 1):
            for coin in coins:
                if i - coin >= 0 and min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1

        if min_coins[total] != float('inf'):
            return min_coins[total]
        else:
            return -1
    except Exception:
        return -1
