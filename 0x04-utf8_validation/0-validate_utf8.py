#!/usr/bin/python3
"""
This program determines if a data set represents valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determine if data has valid UTF-8 encoding.


    Args:
        data (list): A list of integers representing a data set.

    Returns:
        bool: True if the data has valid UTF-8 encoding, False otherwise.
    """
    # Clean each byte by retaining only the 8 least significant bits.
    cleaned_bytes = [raw_byte & 0b11111111 for raw_byte in data]

    # Convert the cleaned bytes to a byte object.
    byte_data = bytes(cleaned_bytes)

    # Attempt to decode the byte data.
    try:
        byte_data.decode()
    except UnicodeDecodeError:
        # If decoding fails, return False indicating invalid UTF-8 encoding.
        return False

    return True
