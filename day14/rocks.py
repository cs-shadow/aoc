import sys
from pprint import pp

matrix = []
for line in sys.stdin.readlines():
    matrix.append(list(line.strip()))
height, width = len(matrix), len(matrix[0])

for j in range(width):
    empty = None
    for i in range(height):
        current = matrix[i][j]
        if current == ".":
            if empty is None:
                empty = i
        elif current == "#":
            empty = None
        else:
            if empty is not None:
                matrix[empty][j] = "O"
                matrix[i][j] = "."
                empty += 1
            else:
                empty = None

total = 0
for idx, line in enumerate(matrix):
    factor = height - idx
    total += factor * line.count("O")

print(total)
