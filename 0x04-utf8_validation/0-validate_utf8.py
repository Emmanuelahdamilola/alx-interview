#!/usr/bin/python3
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    :param data: list of integers representing bytes of data
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    # Count of bytes to follow for the current byte
    bytes_to_follow = 0

    for byte in data:
        # Check if the byte is a continuation byte
        if bytes_to_follow:
            # If the byte doesn't start with 10xxxxxx, it's invalid
            if byte >> 6 != 0b10:
                return False
            bytes_to_follow -= 1
        else:
            # Determine the number of bytes to follow for this byte
            if byte >> 7 == 0:
                bytes_to_follow = 0
            elif byte >> 5 == 0b110:
                bytes_to_follow = 1
            elif byte >> 4 == 0b1110:
                bytes_to_follow = 2
            elif byte >> 3 == 0b11110:
                bytes_to_follow = 3
            else:
                return False

    # If there are still bytes to follow, it's invalid
    return bytes_to_follow == 0

