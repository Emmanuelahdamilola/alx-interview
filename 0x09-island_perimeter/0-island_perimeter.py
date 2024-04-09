#!/usr/bin/python3
"""Island Perimeter Finder.

This script calculates the perimeter of an "island" represented by 1s 
surrounded by "ocean" represented by 0s in a 2D grid.

"""


def island_perimeter(grid):
    """Calculate the perimeter of an island.

    Args:
        grid_map (list of lists of ints): 2D list representation of the island map,
            with 1s representing "land" and 0s representing "water".

    Returns:
        int: Total length of cells around the island's edge.

    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                if col == 0 or not grid[row][col - 1]:
                    perimeter += 1
                if col == len(grid[0]) - 1 or not grid[row][col + 1]:
                    perimeter += 1
                if row == 0 or not grid[row - 1][col]:
                    perimeter += 1
                if row == len(grid) - 1 or not grid[row + 1][col]:
                    perimeter += 1
    return perimeter

