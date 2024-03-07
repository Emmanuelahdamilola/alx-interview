#!/usr/bin/python3


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Mask to check the 2 most significant bits in a byte
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Check each byte in the data
    for byte in data:
        # Mask to check the 3 most significant bits in a byte
        mask = 1 << 7

        # If this byte is the start of a new UTF-8 character
        if num_bytes == 0:
            # Count the number of leading 1s in the byte
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # If this is not a valid UTF-8 character start byte
            if num_bytes == 0:
                continue

            # A UTF-8 character can be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # Check if the byte is following the format 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of remaining bytes for this character
        num_bytes -= 1

    # If all bytes are valid UTF-8 characters
    return num_bytes == 0

