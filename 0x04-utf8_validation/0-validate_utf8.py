#!/usr/bin/python3

def validUTF8(data):
    # Helper function to check if a given byte is a valid start of a UTF-8 character
    def is_start_of_char(byte):
        return (byte & 0b10000000) == 0b00000000 or (byte & 0b11100000) == 0b11000000 or (byte & 0b11110000) == 0b11100000 or (byte & 0b11111000) == 0b11110000

    # Variable to keep track of remaining bytes for a multi-byte character
    remaining_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        # If it's the start of a new character
        if remaining_bytes == 0:
            if not is_start_of_char(byte):
                return False

            # Determine the number of remaining bytes for this character
            if (byte & 0b11100000) == 0b11000000:
                remaining_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                remaining_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                remaining_bytes = 3
        else:
            # If it's a continuation byte
            if (byte & 0b11000000) == 0b10000000:
                remaining_bytes -= 1
            else:
                return False

    # Check if there are remaining bytes at the end of the data
    return remaining_bytes == 0
