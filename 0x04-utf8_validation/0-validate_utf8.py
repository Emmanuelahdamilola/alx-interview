#!/usr/bin/python3


def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding.

    Parameters:
    - data (list): A list of integers representing the bytes of the data set.
                  Each integer represents 1 byte of data, focusing on the 8 least significant bits.

    Returns:
    - bool: True if data is a valid UTF-8 encoding, False otherwise.

    UTF-8 Encoding Rules:
    - A character in UTF-8 can be 1 to 4 bytes long.
    - The data set can contain multiple characters.
    - Each integer represents 1 byte of data, and only the 8 least significant bits are considered.

    Algorithm Overview:
    - Iterate through each integer in the data set.
    - Check if the integer is within the valid range (1 to 4 bytes).
    - For the first byte of a character:
        - Count the number of leading 1s in the binary representation to determine the number of remaining bytes.
        - Validate the start byte and decrement the remaining bytes for the start byte.
    - For continuation bytes:
        - Check if the current byte is a valid continuation byte.
        - Decrement the remaining bytes for continuation bytes.
    - Return True if all bytes are processed and no remaining bytes, else return False.
    """

    # Initialize a variable to keep track of the number of remaining bytes
    remaining_bytes = 0

    # Iterate through each integer in the data
    for num in data:
        # Check if the integer is within the valid range (1 to 4 bytes)
        if num < 0 or num > 255:
            return False

        # If no remaining bytes, check the first byte
        if remaining_bytes == 0:
            # Count the number of leading 1s in the binary representation
            mask = 1 << 7
            while mask & num:
                remaining_bytes += 1
                mask >>= 1

            # Invalid start byte
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

            # Decrement the remaining bytes for the start byte
            remaining_bytes -= 1
        else:
            # Check if the current byte is a continuation byte
            if (num >> 6) != 2:
                return False
            remaining_bytes -= 1

    # All bytes processed, and no remaining bytes
    return remaining_bytes == 0
