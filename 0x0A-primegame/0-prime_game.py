#!/usr/bin/python3
"""Prime Game
"""


def isWinner(x, nums):
    """
    Determine the winner of games where players remove prime numbers
    and their multiples from a set of consecutive integers.

    Args:
    - x (int): The number of rounds/games to be played.
    - nums: list of integers representing the upper bounds for each round

    Returns:
    - str or None: The name of the player who won the most rounds,
      or None if the winner cannot be determined.
    """

    def is_prime(num):
        """
        Check if a number is prime.

        Args:
        - num (int): The number to check.

        Returns:
        - bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def next_prime(start):
        """
        Find the next prime number starting from a given number.

        Args:
        - start (int): The starting number.

        Returns:
        - int: The next prime number after 'start'.
        """
        while True:
            if is_prime(start):
                return start
            start += 1

    def winner(n):
        """
        Simulate the game for a given upper bound and determine the winner.

        Args:
        - n (int): The upper bound of consecutive integers for the game.

        Returns:
        - int: 0 for Maria's win, 1 for Ben's win.
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        primes = [i for i in range(n + 1) if primes[i]]

        turn = 0
        while n > 0:
            n -= next_prime(n)
            turn = 1 - turn

        return turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        result = winner(n)
        if result == 0:
            maria_wins += 1
        elif result == 1:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
