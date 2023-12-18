import sys
from pprint import pp

universe = [list(line.strip()) for line in sys.stdin.readlines()]
mulit_factor = int(sys.argv[1]) - 1
height = len(universe)
width = len(universe[0])

# find emmpties
empty_rows = []
for idx, row in enumerate(universe):
    if all([x == "." for x in row]):
        empty_rows.append(idx)
empty_cols = []
for col in range(width):
    if all([universe[row][col] == "." for row in range(height)]):
        empty_cols.append(col)

# find galaxies
galaxies = []
for row in range(height):
    for col in range(width):
        if universe[row][col] == "#":
            galaxies.append((row, col))

def empty_rows_between(x1, x2):
    if x1 > x2:
        x1, x2 = x2, x1
    count = 0
    for row in empty_rows:
        if x1 < row and row < x2:
            count += 1
    return count

def empty_cols_between(x1, x2):
    if x1 > x2:
        x1, x2 = x2, x1
    count = 0
    for col in empty_cols:
        if x1 < col and col < x2:
            count += 1
    return count

# count
total = 0
for gala in galaxies:
    for galb in galaxies:
        total += abs(gala[0] - galb[0]) + abs(gala[1] - galb[1])
        total += mulit_factor * empty_rows_between(gala[0], galb[0])
        total += mulit_factor * empty_cols_between(gala[1], galb[1])

print(int(total / 2))
