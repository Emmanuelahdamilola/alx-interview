#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    - n (int): Number of rows in Pascal's triangle.

    Returns:
    - List of lists of integers representing Pascal's triangle.

    Note:
    - Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row [1]
    triangle = [[1]]

    # Generate each subsequent row based on the previous row
    for i in range(1, n):
        row = [1]  # Each row starts and ends with 1

        # Compute values for the inner elements of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)  # Each row ends with 1
        triangle.append(row)

    return triangle
