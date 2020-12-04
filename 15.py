"""
Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

1-1-1   1-1 0   1-1 0
    |     |       |
0 0 1   0 1-1   0 1 0
    V       V     |
0 0 1   0 0 1   0 1>1

1 0 0   1 0 0   1 0 0
|       |       |
1-1-1   1-1 0   1 0 0
    V     |     |
0 0 1   0 1>1   1-1>1

How many such routes are there through a 20×20 grid?
"""

size = 20


def initial_solve(width, height):
    cache = {}

    def lattice(width, height):
        nonlocal cache

        if width == 1 or height == 1:
            return 1

        if (width, height) not in cache:
            current = 0

            current += lattice(width - 1, height)
            current += lattice(width, height - 1)

            cache[width, height] = current

        return cache[width, height]

    return lattice(width + 1, height + 1)


def improved_solve(width, height):
    pass


def cheaty_solve(width, height):
    pass


# 837799
print(initial_solve(size, size))
# print(improved_solve(size, size))
# print(cheaty_solve(size, size))
